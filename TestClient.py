#!/usr/bin/python
# -*- coding: utf-8 -*- 
 
import sys
sys.path.append('./gen-py')
 
import os	
import logging
from logging import handlers

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

from LanguageTranslationService.ttypes import * 
import LanguageTranslationService.LTService as lts 
from LanguageTranslator import LanguageTranslator

CURRENT_PATH = os.path.realpath(os.path.dirname(__file__))
LOG_DIR = os.path.join(CURRENT_PATH, 'logs')                            
LOG_FILE = os.path.join(LOG_DIR, 'logget.log')  
LOG_LEVEL = logging.INFO
FORMAT = ('%(asctime)s\t%(message)s') 
DATE_FORMAT = '%d-%m-%Y %H:%M:%S'


if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt=DATE_FORMAT)   

fileHandler = logging.handlers.RotatingFileHandler(filename = LOG_FILE, mode='a+', maxBytes = 1000000, backupCount = 1) 
fileHandler.setFormatter(logging.Formatter(FORMAT, datefmt =DATE_FORMAT))
logging.getLogger().addHandler(fileHandler)

log = logging.getLogger(__name__)


# Метод проверяет работу сервиса переводов
def RunTest():  
l	log.info("run test")
	host = 'localhost'
	port = 9900	 


	# Настраиваем соединение		
	transport = TSocket.TSocket(host, port)   
	transport = TTransport.TBufferedTransport(transport)
	protocol = TCompactProtocol.TCompactProtocol(transport)
	client = lts.Client(protocol)
	
	# Открываем соединение
	transport.open()

	# Получаем перевод
	translatePackage = client.Translate(u"Kingdoms")
	
	# Выводим все поля у полученной структуры с результатом перевода	
	print "Word:\t\t%s" % (translatePackage.word)
	print "Lemma:\t\t%s" % (translatePackage.lemma)
	print "Part Of Speech:\t%s" % (PartOfSpeech.ValueToNames[translatePackage.partOfSpeech])
	for item in translatePackage.translations:
		print "#######################################################" 
		print "Name of the Dictionary:\t%s" % (item.nameDictionary)
		print "Sequence Type:\t%s" % (item.sameTypeSequence)
		print "Translate:\t%s" % (item.translate)	
		
			
	# Закрываем соединение		
	transport.close()

  
if __name__ == "__main__":
	RunTest()   
