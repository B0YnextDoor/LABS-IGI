from utils import validateNumberInput
from task5.matrix import Matrix


class Task5(Matrix):
    def __init__(self) -> None:
        ''' Inits class object. '''
        self.matrix = None

    def __call__(self) -> None | str:
        ''' Runs class methods. '''
        self.validateInput()
        if self.matrix is None:
            return 'stop'
        self.analiseMatrix()

    def validateInput(self) -> None:
        ''' Method validates number of matrix rows & columns input. '''
        rows = validateNumberInput('number of matrix rows (0 -> Exit function)',
                                   'number must be bigger 0', int, condition=lambda x: x < 0)
        if rows == 0:
            self.matrix = None
            return
        columns = validateNumberInput('number of matrix columns',
                                      'number must be bigger 0', int, condition=lambda x: x <= 0)
        super().__call__(rows, columns)

    def printArray(self, array, number: float):
        ''' Method returns numpy array of elements greater then `number`. '''
        print(f'Ammount of elements greater then {number}: {len(array)}')
        if len(array) > 0:
            print('Elements:')
            for el in array:
                print(el, end=" ")
        print()

    def analiseMatrix(self):
        ''' Method analises matrix. '''
        number = validateNumberInput('any number', '', float)
        C = self.findElements(number)
        self.printArray(C, number)
        if len(C) == 0:
            print('Array `C` is empty! Can\'t find median!')
            return
        print(f'NumPy median -> {self.findMedianNp(C)}')
        print(f'Programmed median -> {self.findMedian(C)}')
