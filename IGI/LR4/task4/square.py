from task4.geometricFigure import GeometricFigure
from task4.figureColor import FigureColor
from task4.figureMixin import FigureMixin


class Square(GeometricFigure, FigureMixin):
    def __init__(self, side: float, color: str) -> None:
        ''' Inits class object. '''
        self.side = side
        self.color = FigureColor(color)

    def area(self) -> float:
        ''' Method returns square area. '''
        return self.side**2

    @property
    def name(self) -> str:
        ''' Square name getter. '''
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        ''' Square name setter. '''
        self._name = value.capitalize()
