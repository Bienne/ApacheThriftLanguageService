#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys
sys.path.append('../gen-py')

from WordNet.BaseWordNetItem import BaseWordNetItem
from LanguageTranslationService.ttypes import PartOfSpeech

# Класс для нормалзации наречий
# Класс наследуется от BaseWordNetItem

class WordNetAdverb(BaseWordNetItem):
	def __init__(self, pathToWordNetDict):
	
		# Конструктор родителя (BaseWordNetItem)
		BaseWordNetItem.__init__(self, pathToWordNetDict, 'adv.exc', 'index.adv')
		
		# Часть речи
		self.partOfSpeech = PartOfSpeech.Adverb		
		
		# У наречий есть только списки исключений(adv.exc) и итоговый список слов(index.adv).	
		# Правила замены окончаний при нормализации слова по правилам у наречий нет. 


			
