from math import log
from task3.rowAnaliser import RowAnaliser


class TailorSum(RowAnaliser):
    def __init__(self) -> None:
        ''' Inits class object. '''
        super().__init__()

    def __call__(self):
        ''' Clears list with row elements. '''
        self.row.clear()

    def countMath(self, x: float):
        ''' Method returns function value in the x point. '''
        return log((x + 1)/(x - 1))

    def countTailor(self, x: float, eps: float, mathResult: float) -> tuple[float, int]:
        ''' Function that counts sum of Tailor's row with the required accuracy. '''
        tailorSum = 0
        N = -1
        while N + 1 < 500:
            N += 1
            element = 1/((2*N+1)*x**(2*N+1))
            tailorSum += element
            if (abs(2*tailorSum - mathResult) >= eps/10):
                continue
            break
        self.row.append(2*tailorSum)
        return 2*tailorSum, N+1

    def getAdditionalParams(self) -> str:
        ''' Function returns additional parameters of sequence. '''
        params = super().__call__()
        if type(params) == str:
            return params
        print(f'Mode: {params[2]}\n')
        return f'Additional parameters:\nArithmetics mean: {params[0]}\n\
Median: {params[1]}\nVariance: {params[3]}\nStandard deviation: {params[4]}'
