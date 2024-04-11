import re
from collections import Counter
from task2.baseAnaliser import Analiser


class TextAnaliser(Analiser):
    def __init__(self, text: str):
        ''' Inits class object. '''
        self.text = text
        self.sentences = re.split(r'(?<=[.!?])\s', text)
        self.words = re.findall(r'\w+', self.text)

    def countSentences(self) -> int:
        ''' Method returns amount of sentences. '''
        return len(self.sentences)

    def countTypesSentences(self) -> tuple[int, int, int]:
        ''' Method returns amount of each type sentence. '''
        return (len([1 for sent in self.sentences if sent.endswith('.')]),
                len([1 for sent in self.sentences if sent.endswith('?')]),
                len([1 for sent in self.sentences if sent.endswith('!')]))

    def avgSentenceLen(self) -> float:
        ''' Method returns average sentence length. '''
        sentence_lengths = [len(word) for word in self.words]
        return round(sum(sentence_lengths) / len(self.sentences), 3) if self.sentences else 0

    def avgWordLen(self) -> float:
        ''' Method return average word length. '''
        words_lengths = [len(word) for word in self.words]
        return round(sum(words_lengths) / len(self.words), 3) if self.words else 0

    def countSmiles(self) -> int:
        ''' Method returns ammount of smiles in the text. '''
        return len(re.findall(r'[:;]-*[()\[\]]+', self.text))

    def getMatchWords(self) -> list[str]:
        ''' Method returns words with letters from \'a\' to \'o\' or digits. '''
        return re.findall(r'\b\w*([a-o]+\w*\d+|\d+\w*[a-o]+)\w*\b', self.text)

    def checkStr(self, input_string: str) -> bool:
        ''' Method checks if input string is 6-digits number in decimal system without leading zeros. '''
        return bool(re.match(r'^[1-9]\d{5}$', input_string))

    def countQuotesWords(self) -> int:
        ''' Method returns amount of words in quotes. '''
        return len(re.findall(r'\s(\"|\'|«)(.+?)(\"|\'|\»)', self.text))

    def countLetters(self) -> dict[str, int]:
        ''' Method returns amount of each letter in text. '''
        return Counter(re.findall(r'[a-z]', self.text.lower()))

    def getPhrases(self) -> list[str]:
        ''' Method returns phrases in commas from the text. '''
        return sorted([ph[0][2:-1].lower() for ph in re.findall(r'(\,(\s+\w+){2,}\,)', self.text)])
