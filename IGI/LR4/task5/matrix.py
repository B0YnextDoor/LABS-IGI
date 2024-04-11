from generators import matrixGenerator
import numpy as np


class Matrix():
    def __call__(self, rows: int, columns: int) -> None:
        ''' Method generates matrix[rows, columns]. '''
        self.matrix = np.array(matrixGenerator(rows, columns))
        print('Generated matrix:')
        for row in self.matrix:
            print(row)
        print()

    def findElements(self, number: float):
        ''' Method returns numpy array with elements greater then `number`. '''
        return self.matrix[np.abs(self.matrix) > number]

    def findMedianNp(self, array):
        ''' Method counts array median. '''
        return np.median(array)

    def findMedian(self, array) -> float:
        ''' Method counts array median. '''
        array.sort()
        l = len(array)
        return array[l // 2] if l % 2 else (array[l // 2 - 1] + array[l // 2]) / 2
