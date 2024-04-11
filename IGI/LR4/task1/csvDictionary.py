import csv
from task1.baseDictionary import BaseDictionary, synonyms_dict


class CsvDictionary(BaseDictionary):
    def __init__(self, FILENAME: str) -> None:
        ''' Inits class object. '''
        super().__init__(FILENAME)
        with open(FILENAME, "w", newline='') as file:
            csv.writer(file).writerows(
                {k: synonyms_dict[k] for k in sorted(synonyms_dict)}.items())

    def getDictionary(self) -> dict[str, str]:
        ''' Method returns dictionary from csv file. '''
        with open(self.filename, 'r', newline='\n') as file:
            reader = csv.reader(file)
            synonyms: dict[str, str] = dict()
            for row in reader:
                synonyms[row[0]] = row[1]
            return synonyms
