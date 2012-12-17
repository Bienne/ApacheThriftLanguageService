namespace py LanguageTranslationService
 
enum PartOfSpeech 
{
	Adjective = 1,
	Adverb = 2,
	Noun = 3,
	Verb = 4 
} 

struct TranslateOneDictionary
{
  1: string nameDictionary,
  2: string translate,
  3: string sameTypeSequence,
}
 
struct TranslatePackage  
{
  1: string word,
  2: string lemma,
  3: PartOfSpeech partOfSpeech,
  4: list<TranslateOneDictionary> translations 
}

exception InvalidValueException 
{
  1: i32 errorCode,
  2: string errorMsg
}


service LTService 
{
  TranslatePackage Translate(1:string word) throws (1: InvalidValueException e),
}
