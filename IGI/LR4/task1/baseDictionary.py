synonyms_dict = dict([["быстрый", "скорый"],
                      ["медленный", "неспешный"],
                      ["умный", "интеллектуальный"],
                      ["глупый", "неразумный"],
                      ["смелый", "отважный"],
                      ["трусливый", "боязливый"]])


class BaseDictionary():
    def __init__(self, FILENAME: str) -> None:
        ''' Inits class object. '''
        self.filename = FILENAME

    def getDictionary(self) -> dict[str, str]:
        ''' Method returns dictionary from the file. '''
        pass

    def getLastSynonym(self) -> str:
        ''' Method returns last word-synonym from the dictionary. '''
        return list(self.getDictionary().values())[-1]

    def getWordInfo(self, word: str) -> None:
        ''' Method returns info about the word according on the file. '''
        dictionary = self.getDictionary()
        values: list[str] = list(dictionary.values())
        if word in values:
            try:
                print(
                    f'Pair: {list(dictionary.keys())[values.index(word)]} - {word}')
            except ValueError:
                print('Word isn\'t found!')
            finally:
                return
        synonym: str | None = dictionary.get(word)
        print(
            f'Pair: {word} - {synonym}' if synonym is not None else 'Word isn\'t found!')
