#!/usr/bin/python
# -*- coding: utf-8 -*- 
 
import sys
sys.path.append('./gen-py')
 
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

from LanguageTranslationService.ttypes import * 
import LanguageTranslationService.LTService as lts 
from LanguageTranslator import LanguageTranslator
# Метод проверяет работу сервиса переводов
def RunTest():  
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
