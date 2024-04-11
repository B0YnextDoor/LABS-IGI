from task4.geometricFigure import GeometricFigure
from task4.figureColor import FigureColor
from task4.figureMixin import FigureMixin
from math import sqrt


class Triangle(GeometricFigure, FigureMixin):
    def __init__(self, side: float, color: str) -> None:
        ''' Inits class object. '''
        self.side = side
        self.color = FigureColor(color)

    def area(self) -> float:
        ''' Method returns triangle area. '''
        return self.side**2 * sqrt(3)/4

    @property
    def name(self) -> str:
        ''' Triangle name getter. '''
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        ''' Triangle name setter. '''
        self._name = value.capitalize()
