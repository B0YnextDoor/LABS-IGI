from task1.csvDictionary import CsvDictionary
from task1.pickleDictionary import PickleDictionary
from utils import stopFunction


class Task1():
    def __init__(self) -> None:
        ''' Inits object of the class. '''
        self.path = './task1/file.'

    def __call__(self, dictionary: CsvDictionary | PickleDictionary) -> None:
        ''' Runs class methods. '''
        self.printDictionary(dictionary)
        self.getLastWord(dictionary)
        dictionary.sortDictionary()
        self.printDictionary(dictionary, 'Sorted ')
        self.getLastWord(dictionary)
        self.getWordInfo(dictionary)

    def printDictionary(self, dictionary: CsvDictionary | PickleDictionary, msg: str = '') -> None:
        ''' Method returns loaded from file dictionary. '''
        print(f'{msg}Dictionary:')
        for words in dictionary.getDictionary().items():
            print(f'{words[0]} - {words[1]}')
        print()

    def getLastWord(self, dictionary: CsvDictionary | PickleDictionary) -> None:
        ''' Method returns last word-synonym from dictionary. '''
        print('Last word-synonym:')
        print(f'{dictionary.getLastSynonym()}')
        print()

    def getWordInfo(self, dictionary: CsvDictionary | PickleDictionary) -> None:
        ''' Method returns word\'s synonym from the dictionary if it\'s possible. '''
        while True:
            word = input('Enter word to find: ')
            dictionary.getWordInfo(word)
            print()
            if stopFunction() == '0':
                break
