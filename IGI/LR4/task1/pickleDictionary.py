import pickle
from task1.baseDictionary import BaseDictionary, synonyms_dict


class PickleDictionary(BaseDictionary):
    def __init__(self, FILENAME: str) -> None:
        ''' Inits class object. '''
        super().__init__(FILENAME)
        with open(FILENAME, 'wb') as file:
            pickle.dump({k: synonyms_dict[k]
                        for k in sorted(synonyms_dict)}, file)

    def getDictionary(self) -> dict[str, str]:
        ''' Method returns dictionary from pkl file. '''
        with open(self.filename, 'rb') as file:
            return pickle.load(file)
