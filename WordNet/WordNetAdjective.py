#!/usr/bin/python
# -*- coding: utf-8 -*- 
import sys
sys.path.append('../gen-py')

from WordNet.BaseWordNetItem import BaseWordNetItem
from LanguageTranslationService.ttypes import PartOfSpeech

# Класс для работы с нормализацией прилагательных
# Класс наследуется от BaseWordNetItem

class WordNetAdjective(BaseWordNetItem):
	def __init__(self, pathToWordNetDict):
	
		# Конструктор родителя (BaseWordNetItem)
		BaseWordNetItem.__init__(self, pathToWordNetDict, 'adj.exc', 'index.adj')
		
		# Часть речи
		self.partOfSpeech = PartOfSpeech.Adjective

		# Правила замены окончаний при нормализации слова по правилам. К примеру, окончание "er" заменяется на "" или  "e" и тд.
		self.rule = (	
						["er"  , "" ],
						["er"  , "e"],
						["est" , "" ], 			
						["est" , "e"]	
					)

						
		# Метод получения нормализованной формы слова GetLemma(word) определен в базовом классе BaseWordNetItem
