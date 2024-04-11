from task2.textAnaliser import TextAnaliser
from task2.baseAnaliser import Analiser
from utils import validateNumberInput
from zipfile import ZIP_DEFLATED, ZipFile
from datetime import datetime


class Task2(Analiser):
    _border: str = ('*' * 80) + "\n"

    def __init__(self) -> None:
        ''' Inits class object. '''
        self.path = './task2/'
        self.results: list[str] = list()
        with open(f'{self.path}file.txt', 'r', encoding='utf-8') as file:
            text = file.read()
        self.analiser = TextAnaliser(text)

    def __call__(self) -> None:
        ''' Runs class methods. '''
        self.results.clear()
        self.countSentences()
        self.countTypesSentences()
        self.avgSentenceLen()
        self.avgWordLen()
        self.countSmiles()
        self.getMatchWords()
        self.checkStr()
        self.countQuotesWords()
        self.countLetters()
        self.countPhrases()
        self.saveResults()
        self.zipFile()

    def countSentences(self) -> None:
        ''' Method returns ammount of sentences in the text. '''
        self.results.append(
            f'Sentenses ammount: {self.analiser.countSentences()}\n' + self._border)

    def countTypesSentences(self) -> None:
        ''' Method returns ammount of each type sentence. '''
        ammount = self.analiser.countTypesSentences()
        self.results.append(f'''Declarative sentenses ammount: {ammount[0]}
Interrogative sentences ammount: {ammount[1]}
Incentive sentenses ammount: {ammount[2]}\n''' + self._border)

    def avgSentenceLen(self) -> None:
        ''' Method returns average sentence length. '''
        self.results.append(
            f'Average sentence length: {self.analiser.avgSentenceLen()}\n' + self._border)

    def avgWordLen(self) -> None:
        ''' Method return average word length. '''
        self.results.append(
            f'Average word length: {self.analiser.avgWordLen()}\n' + self._border)

    def countSmiles(self) -> None:
        ''' Method returns ammount of smiles in the text. '''
        self.results.append(
            f'Ammount of smiles: {self.analiser.countSmiles()}\n' + self._border)

    def getMatchWords(self) -> None:
        ''' Method returns words with letters from \'a\' to \'o\' or digits. '''
        result_str = 'Words with letters from \'a\' to \'o\' and digits:\n'
        for word in self.analiser.getMatchWords():
            result_str += word + "\n"
        self.results.append(result_str + self._border)

    def checkStr(self) -> None:
        ''' Method checks if input string is 6-digits number in decimal system without leading zeros. '''
        input_string = str(validateNumberInput(
            'integer number string', '', int))
        res = '' if self.analiser.checkStr(input_string) else ' not'
        self.results.append(
            f'String {input_string} is{res} valid\n' + self._border)
        print()

    def countQuotesWords(self) -> None:
        ''' Method returns amount of words in quotes. '''
        self.results.append(
            f'Ammount of words in quotes: {self.analiser.countQuotesWords()}\n' + self._border)

    def countLetters(self) -> None:
        ''' Method returns amount of each letter in text. '''
        result_str = 'Ammount of each letter:\n'
        for res in self.analiser.countLetters().items():
            result_str += f'{res[0]} - {res[1]}\n'
        self.results.append(result_str + self._border)

    def countPhrases(self) -> None:
        ''' Method returns phrases in commas from the text. '''
        result_str = 'Phrases in commas:\n'
        for phrase in self.analiser.getPhrases():
            result_str += phrase + "\n"
        self.results.append(result_str + self._border)

    def saveResults(self) -> None:
        ''' Method saves results to a file. '''
        print('Analised text:')
        print(self.analiser.text)
        print("\nResults:")
        with open(f'{self.path}results.txt', 'w', newline='\n', encoding='utf-8') as file:
            for res in self.results:
                file.write(res)
                print(res)

    def zipFile(self) -> None:
        ''' Method zips results. '''
        with ZipFile(f'{self.path}results.zip', 'w', compression=ZIP_DEFLATED) as file:
            file.write(f'{self.path}results.txt')
            print('Zip file info:')
            for item in file.infolist():
                print(f'Filename: {item.filename}')
                print(f'''Last change: {datetime(item.date_time[0], item.date_time[1], item.date_time[2],
                                               item.date_time[3], item.date_time[4], item.date_time[5])}''')
                print(f'Compress type: {item.compress_type}')
                print(f'Compress size: {item.compress_size}')
                print(f'File size: {item.file_size}')
