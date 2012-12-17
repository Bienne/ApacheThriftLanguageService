#!/usr/bin/python
# -*- coding: utf-8 -*- 


from WordNet.WordNetAdjective import WordNetAdjective
from WordNet.WordNetAdverb import WordNetAdverb
from WordNet.WordNetNoun import WordNetNoun
from WordNet.WordNetVerb import WordNetVerb

class Lemmatizer:
	def __init__(self, pathToWordNetDict):
	
		# Разделитель составных слов	
		self.splitter = "-" 						
		
		# Инициализируем объекты с частям речи
		adj = WordNetAdjective(pathToWordNetDict)	# Прилагательные
		noun = WordNetNoun(pathToWordNetDict)		# Существительные
		adverb = WordNetAdverb(pathToWordNetDict)	# Наречия
		verb = WordNetVerb(pathToWordNetDict)		# Глаголы
		
		self.wordNet = [verb, noun, adj, adverb]
		

	# Метод возвращает лемму слова (возможно, составного)		
	def GetLemma(self, word):
		# Если в слове есть тире, разделим слово на части, нормализуем каждую часть(каждое слово) по отдельности, а потом соединим
		wordArr = word.split(self.splitter)
		resultWord = []
		for word in wordArr:
			lemma, partOfSpeech = self.__GetLemmaWord(word)
			if (lemma != None):
				resultWord.append(lemma)
		if (resultWord != None):
			return [self.splitter.join(resultWord), partOfSpeech]
		return None		
		
		
		
	# Метод возвращает лемму(нормализованную форму слова)			
	def __GetLemmaWord(self, word):
		for item in self.wordNet:
			lemma = item.GetLemma(word)
			if (lemma != None):
				return [lemma, item.partOfSpeech]
		return None		
			
			
