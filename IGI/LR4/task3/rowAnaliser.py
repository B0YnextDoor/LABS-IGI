from statistics import fmean, median, mode, variance, stdev


class RowAnaliser():
    def __init__(self) -> None:
        ''' Inits class object. '''
        self.row: list[float] = list()

    def __call__(self) -> tuple[float, float, float, float, float] | str:
        ''' Runs class methods. '''
        if len(self.row) == 0:
            return 'Tailor\'s row is empty!'
        return (self.mean(), self.median(), self.mode(), self.variance(), self.stdev())

    def mean(self) -> float | str:
        ''' Method counts arithmetic mean of sequence. '''
        return round(fmean(self.row), 4) if len(self.row) > 0 else 'Tailor\'s row is empty!'

    def median(self) -> float | str:
        ''' Method returns sequence median. '''
        return round(median(self.row), 4) if len(self.row) > 0 else 'Tailor\'s row is empty!'

    def mode(self) -> float | str:
        ''' Method returns sequence mode. '''
        return round(mode(self.row), 4) if len(self.row) > 0 else 'Tailor\'s row is empty!'

    def variance(self) -> float | str:
        ''' Method counts sequence variance. '''
        if len(self.row) == 0:
            return 'Tailor\'s row is empty!'
        elif len(self.row) < 2:
            return 'Can\'t find variance. 2 and more elements needed.'
        return round(variance(self.row), 4)

    def stdev(self) -> float | str:
        ''' Method counts standart deviance of sequence. '''
        if len(self.row) == 0:
            return 'Tailor\'s row is empty!'
        elif len(self.row) < 2:
            return 'Can\'t find standart deviance. 2 and more elements needed.'
        return round(stdev(self.row), 4)
