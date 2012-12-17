#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
sys.path.append('./../gen-py')

from Ifo import Ifo
from Idx import Idx
from Dict import Dict
from LanguageTranslationService.ttypes import *

class StarDict:
	def __init__(self, pathToDict):

		try:
			# Формат словаря DICT предусматривает 3 обязательных файла (.ifo, .idx, .dict) и 1 необязательный (.syn)
			# Если хотя бы один из обязательных словарей отсутствует, вызовется исключение и словарь не будет загружен

			# Создаем объект Ifo (он содержит настройки и мета-информацию о словаре) [Обязательный файл]
			self.Ifo = Ifo(pathToDict)
			
			# Создаем объект Idx (он содержит отсортированный список всех слов и оффсеты для каждого слова в файле .dict) [Обязательный файл]
			self.Idx = Idx(pathToDict, self.Ifo.wordCount, self.Ifo.idxFileSize, self.Ifo.idxOffsetBits)
	
			# Создаем объект Dict (он содержит текстовую информацией (сами слова, транскрипцию, значение), дополненную различными медиа-файлами и разметками других словарных форматов) [Обязательный файл]
			self.Dict = Dict(pathToDict, self.Ifo.sameTypeSequence)
			
			# Название словаря
			self.bookName = self.Ifo.bookName
			
			# Маркер, определяющий форматирование словарной статьи
			self.sameTypeSequence = self.Ifo.sameTypeSequence			
			
		except Exception as e:
				raise Exception('Dictionary "%s" was not loaded: %s' %(pathToDict, e))

				
				
	def Translate(self, word):
	
		# Приводим слово к нижнему регистру и убираем пробелы с начала и конца
		word = word.lower().strip() 
		
		# Получаем у объекта Idx координаты расположения слова внутри файла .dict
		wordDataOffset, wordDataSize  = self.Idx.GetLocationWord(word)
		if wordDataOffset == "" or wordDataSize == "":
			return None
			
		# Получаем у объекта Dict сам перевод и возвращаем его	
		valueTranslate = self.Dict.GetTranslation(wordDataOffset, wordDataSize)	 
		return TranslateOneDictionary(self.bookName, valueTranslate, self.sameTypeSequence)
		
				

	
	
			
			
