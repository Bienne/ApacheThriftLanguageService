#!/usr/bin/python
# -*- coding: utf-8 -*- 

import cPickle

class Dumper:
	def __init__(self):
		pass
			
	# Метод создает дамп объекта 
	def CreateDump(self, fileForSaving, object):	
		try:	
			with open(fileForSaving, 'wb') as file:
				cPickle.dump(object, file)			
		except Exception as e:
			raise Exception('Pickling error: "%s"' %e)


	# Метод загружает дамп объекта
	def LoadDump(self, loadingFile):	
		try:	
			with open(loadingFile, 'rb') as file:
				return cPickle.load(file)
		except Exception as e:
			raise Exception('Unpickling error: "%s"' %e)
 
