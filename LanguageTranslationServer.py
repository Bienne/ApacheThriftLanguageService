#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
sys.path.append('./gen-py')

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer
import LanguageTranslationService.LTService as lts
from LanguageTranslator import LanguageTranslator

# Метод запускает сервис переводов
def RunLTServer(): 

	sPort = 9900
	
	try:
		processor = lts.Processor(LanguageTranslator())
		transport = TSocket.TServerSocket(port = sPort) 							# Cоздаем сокет сервера и привязываем его к порту 9900
		tfactory = TTransport.TBufferedTransportFactory() 							# Создаем транспорт, использующий буфер для ввода/вывода
		pfactory = TCompactProtocol.TCompactProtocolFactory() 						# Протокол компактного двоичного формата
		server = TServer.TThreadedServer(processor, transport, tfactory, pfactory) 	# Многопоточный сервер

		print 'Starting the server...'
		server.serve()
		print 'done' 	
				
	except Exception as e:
		print e		
    
if __name__ == "__main__":
	RunLTServer()   
