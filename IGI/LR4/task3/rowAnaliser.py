from collections import Counter
from math import sqrt


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
        return round(sum(self.row) / len(self.row), 4) if len(self.row) > 0 else 'Tailor\'s row is empty!'

    def median(self) -> float | str:
        ''' Method returns sequence median. '''
        if len(self.row) == 0:
            return 'Tailor\'s row is empty!'
        sorted_row = sorted(self.row)
        l = len(sorted_row)
        return round(0.5*(sorted_row[l // 2 - 1] + sorted_row[l // 2]) if l % 2 == 0 else sorted_row[l // 2], 4)

    def mode(self) -> str:
        ''' Method returns sequence mode. '''
        if len(self.row) == 0:
            return 'Tailor\'s row is empty!'
        value_counts = Counter(self.row)
        max_count = max(value_counts.values())
        return str([round(value, 4) for value,
                    count in value_counts.items() if count == max_count])

    def variance(self) -> float | str:
        ''' Method counts sequence variance. '''
        if len(self.row) == 0:
            return 'Tailor\'s row is empty!'
        elif len(self.row) < 2:
            return 'Can\'t find variance. 2 and more elements needed.'
        mean = self.mean()
        return round(sum((s - mean) ** 2 for s in self.row) / len(self.row), 4)

    def stdev(self) -> float | str:
        ''' Method counts standart deviance of sequence. '''
        if len(self.row) == 0:
            return 'Tailor\'s row is empty!'
        elif len(self.row) < 2:
            return 'Can\'t find standart deviance. 2 and more elements needed.'
        return round(sqrt(self.variance()), 4)
