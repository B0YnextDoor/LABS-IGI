from abc import ABC


class Analiser(ABC):
    def countSentences(self) -> int:
        ''' Method returns amount of sentences. '''
        pass

    def countTypesSentences(self) -> tuple[int, int, int]:
        ''' Method returns amount of each type sentence. '''
        pass

    def avgSentenceLen(self) -> float:
        ''' Method returns average sentence length. '''
        pass

    def avgWordLen(self) -> float:
        ''' Method return average word length. '''
        pass

    def countSmiles(self) -> int:
        ''' Method returns ammount of smiles in the text. '''
        pass

    def getMatchWords(self) -> list[str]:
        ''' Method returns words with letters from \'a\' to \'o\' or digits. '''
        pass

    def checkStr(self, input_string: str) -> bool:
        ''' Method checks if input string is 6-digits number in decimal system without leading zeros. '''
        pass

    def countQuotesWords(self) -> int:
        ''' Method returns amount of words in quotes. '''
        pass

    def countLetters(self) -> dict[str, int]:
        ''' Method returns amount of each letter in text. '''
        pass

    def getPhrases(self) -> list[str]:
        ''' Method returns phrases in commas from the text. '''
        pass
