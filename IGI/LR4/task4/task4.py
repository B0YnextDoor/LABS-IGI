from utils import validateNumberInput, validateColorInput
from task4.square import Square
from task4.triangle import Triangle, sqrt
from matplotlib import pyplot as plt


class Task4():
    def __init__(self) -> None:
        ''' Inits class object. '''
        self.square = None
        self.triangle = None

    def __call__(self) -> None | str:
        ''' Runs class methods. '''
        self.validateInput()
        if self.square is None:
            return 'stop'
        self.displayInfo()
        self.displayCharts()

    def validateInput(self) -> None:
        ''' Function for validation input of square side. '''
        side = validateNumberInput('length of square side (0 -> Exit function)', 'length must be bigger 0', float,
                                   condition=lambda x: x < 0)
        if side == 0:
            self.square = None
            return
        self.square = Square(side, validateColorInput('square'))
        self.triangle = Triangle(side, validateColorInput('triangle'))
        self.square.name = input('Enter square name: ')
        self.triangle.name = input('Enter triangle name: ')

    def displayInfo(self) -> None:
        ''' Method displays figures info in console. '''
        print('\nSquare info:')
        print(self.square)
        print('\nTriangle info:')
        print(self.triangle)

    def displayCharts(self) -> None:
        ''' Method displays figures charts. '''
        side = self.square.side
        square_x = [0, side, side, 0, 0]
        square_y = [0, 0, side, side, 0]
        triangle_x = [side, side, (sqrt(3)*0.5 + 1)*side, side]
        triangle_y = [0, side, 0.5*side, 0]
        plt.figure()
        plt.xlim(0, (sqrt(3)*0.5 + 1)*side + 1)
        plt.ylim(0, side + 1)
        plt.axis('equal')
        plt.plot(square_x, square_y, color=self.square.color.color, marker='o',
                 markersize=5, linestyle='-')
        plt.plot(triangle_x, triangle_y, color=self.triangle.color.color, marker='o',
                 markersize=5, linestyle='-', label=self.triangle.name)
        plt.annotate(self.square.name, (side/2 -
                     len(self.square.name)*0.1, side/2))
        plt.annotate(self.triangle.name,
                     ((sqrt(3)*0.25 + 1)*side -
                      len(self.triangle.name)*0.1, side/2))
        plt.fill(square_x, square_y, color=self.square.color.color, alpha=0.6)
        plt.fill(triangle_x, triangle_y,
                 color=self.triangle.color.color, alpha=0.6)
        plt.autoscale()
        plt.savefig('./task4/charts.png')
