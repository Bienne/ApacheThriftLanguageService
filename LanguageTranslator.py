#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
sys.path.append('./gen-py')

import os
import re
import cPickle

from IniParser import IniParser
from Dumper import Dumper
from WordNet.Lemmatizer import Lemmatizer
from StarDict.StarDict import StarDict
from LanguageTranslationService.ttypes import *
import LanguageTranslationService.LTService as lts

ConfigFileName="Settings.ini"

class LanguageTranslator(lts.Iface):
	def __init__(self):
	
		try:
			# Определяем регулярное выражение для поиска английских слов
			self.wordPattern = re.compile("^((?:[a-zA-Z]+[-']?)*[a-zA-Z]+)$")
		
			# Создаем и инициализируем конфиг-парсер
			config = IniParser(ConfigFileName)	
			
			# Считываем переменные из конфиг-файлв
			self.workDir = config.GetValue("WorkDir")						# Считываем из ini файла переменную WorkDir, которая содержит рабочую папку транслейтора (для сохранения объектов словарей между запусками скрипта)
			self.pathToWordNetDict = config.GetValue("PathToWordNetDict")	# Считываем из ini файла переменную PathToWordNetDict, которая содержит путь до словаря WordNet
			self.pathToStarDict = config.GetValue("PathToStarDict") 		# Считываем из ini файла переменную PathToStarDict, которая содержит путь до словарей в формате StarDict	
			
 			# Проверим, существует ли рабочая папка транслейтора
			self.__CheckDirExists(self.workDir)		
			
 			# Создадим дампер (с его помощью будем сохранять объекты в дампы и выгружать из дампов)			
			self.dumper = Dumper()
 			
			# Создадим нормализатор слов
			self.lemmatizer = self.__CreateLemmatizer()	
			
			# Создадим словарные базы StarDict			
			self.listStarDictDictionaries = self.__CreateStarDictDictionaries()
			
		except Exception as e:
			raise Exception('Error: "%s"' %e)
			
			
	# Метод переводит слово
	def Translate(self, sourceWord):
		
		# Уберем пробелы и приведем к нижнему регистру		
		word = sourceWord.strip().lower() 
		
		# Слово для перевода не может быть пустой строкой		
		if sourceWord == "":
			raise InvalidValueException(1, 'Empty value')
		
		# Проверим, относится ли слово к английскому 					
		self.__CheckValidEnglishWord(word)

		# Получим лемму слова	
		lemma, partOfSpeech = self.lemmatizer.GetLemma(word) 
		if lemma == None:
			raise InvalidValueException(1, 'Could not get the lemma for a given word')
					
		# Получим переводы со всех словарей
		listTranslations = []
		
		for dict in self.listStarDictDictionaries:
			translateOneDictionary = dict.Translate(lemma)
			if translateOneDictionary != None:
				listTranslations.append(translateOneDictionary)	
					
		return TranslatePackage(sourceWord, lemma, partOfSpeech, listTranslations)

		
		
	# Метод проверяет, является ли текст английским словом
	def __CheckValidEnglishWord(self, sourceWord):
		result = self.wordPattern.search(sourceWord) 
		if not result:				
			raise InvalidValueException(1, 'Invalid word')							
							
					
	# Метод проверяет папку на существование		
	def __CheckDirExists(self, directory):			
		if not os.path.isdir(directory):
			raise Exception('Directory "%s" does not exists' % directory)	
			
			
	# Метод создает нормализатор слов		
	def __CreateLemmatizer(self):			
		lemmatizerDump = 'Lemmatizer.dump' 	# название дампа нормализатора
		pathToLemmatizerDump = os.path.join(self.workDir, lemmatizerDump)	# Полный путь до дампа нормализатора
		
		# Отправляемся в рабочую папку транслейтора за поисками дампа нормализатора
		if os.path.isfile(pathToLemmatizerDump):
			return self.dumper.LoadDump(pathToLemmatizerDump)
		else:
			# Здесь мы понимаем, что дампа нормализатора у нас нет. Значит сперва создадим нормализатор, и затем сохраним его дамп.
			lemmatizer = Lemmatizer(self.pathToWordNetDict)	
			if lemmatizer != None:							 
				self.dumper.CreateDump(pathToLemmatizerDump, lemmatizer)				
			return lemmatizer
				
				
	# Метод создает словарные базы StarDict	
	def __CreateStarDictDictionaries(self):	
		listStarDictDictionaries = []
		
		# Отделяем пути словарей StarDict друг от друга и удаляем пробелы с начала и конца пути. Все пути заносим в список listPathToStarDict
		listPathToStarDict = [item.strip() for item in self.pathToStarDict.split(";")]			
		
		# Для каждого из путей до словарей StarDict создаем свой языковый словарь
		for path in listPathToStarDict:
			languageDict = self.__CreateStarDictDictionary(path)
			if languageDict != None:
				listStarDictDictionaries.append(languageDict) 
			
		return listStarDictDictionaries	


	# Метод создает один словарь StarDict	
	def __CreateStarDictDictionary(self, pathToStarDictDictionary):
		try:
			nameStarDictDump = os.path.basename(pathToStarDictDictionary)		# Из всего пути до StarDict получаем только последнюю папку, она послужит именем дампа  			
			pathToStarDictDump = os.path.join(self.workDir, nameStarDictDump)	# Полный путь до дампа словаря StarDict
			if os.path.isfile(pathToStarDictDump):
				return self.dumper.LoadDump(pathToStarDictDump)
			else:
				languageDict = StarDict(pathToStarDictDictionary)							 
				self.dumper.CreateDump(pathToStarDictDump, languageDict)
				return languageDict					
		except Exception as e:
				# Если при создании словаря или восстановлении его из дампа произошла ошибка - просто исключим словарь 
				# из общего списка загруженных словарей и будем дальше работать с остальными словарями
				print e 
				return None
		
	
	
	
