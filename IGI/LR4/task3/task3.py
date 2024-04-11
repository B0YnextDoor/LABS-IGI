from utils import validateNumberInput
import matplotlib.pyplot as plt
from statistics import median
from task3.tailorSum import TailorSum


class Task3():
    def __init__(self) -> None:
        ''' Inits class object. '''
        self.tailor = TailorSum()
        self.mathResults = list()
        self.tailorResults = list()
        self.iterations = list()

    def __call__(self) -> None | str:
        ''' Runs class methods. '''
        self.validateInput()
        if self.eps == 0:
            return 'stop'
        self.tailor()
        self.displayConsole()
        self.displayCharts()

    def validateInput(self) -> None:
        ''' Method for validation input of accuracy and x value. '''
        self.eps = validateNumberInput(
            'accuracy (0 < acc < 1) (0 -> Exit function)', '0 < acc < 1', float, condition=lambda x: x < 0 or x >= 1)
        if self.eps == 0:
            return
        start = validateNumberInput(
            'start x (|x| > 1)', '|x| must be bigger than 1', float, condition=lambda x: abs(x) <= 1)
        while True:
            end = validateNumberInput(
                'end x (|x| > 1 & x > start)', '|x| must be bigger than 1', float, condition=lambda x: abs(x) <= 1)
            if end <= start:
                print('Wrong input -> (end point > start point)! Try again!\n')
                continue
            break
        N = validateNumberInput(
            'number of points (N > 0)', 'N - integer positive number', int, condition=lambda x: x <= 0)
        h = (end - start) / N
        self.x = [round(start + i*h, 4) for i in range(N + 1)]

    def printBorders(self, type: str, length: int) -> None:
        ''' Method prints result table borders. '''
        for i in range(5):
            if i == 0:
                print("┏━━" + "━" * length,
                      end="━━┳━━") if type == 'top' else print("\n┣━━" + "━" * length, end="━━╋━━") \
                    if type == 'mid' else print("\n┗━━" + "━" * length, end="━━┻━━")
            elif i != 4:
                print("━" * (length + 3), end="━━┳━━") if type == 'top' else print("━" * (length + 3), end="━━╋━━") \
                    if type == 'mid' else print("━" * (length + 3), end="━━┻━━")
            else:
                print("━" * (length + 3), end="━━┓\n") if type == 'top' else print("━" * (length + 3), end="━━┫\n") \
                    if type == 'mid' else print("━" * (length + 3), end="━━┛\n")

    def displayConsole(self) -> None:
        ''' Method displays the result in console. '''
        for x in self.x:
            self.mathResults.append(self.tailor.countMath(x))
            tailorSum, iterations = self.tailor.countTailor(
                x, self.eps, self.mathResults[-1])
            self.tailorResults.append(tailorSum)
            self.iterations.append(iterations)
        length = max(len(str(max(self.tailorResults))), len(str(max(self.iterations))),
                     len((str(self.eps))), len(str(max(self.x))), 9)
        data = [["x", "n", "F(x)", "Math F(x)", "eps"]]
        for i in range(len(self.x)):
            data.append([self.x[i], self.iterations[i], round(self.tailorResults[i], len(str(self.eps))),
                         round(self.mathResults[i], len(str(self.eps))), self.eps])
        self.printBorders('top', length)
        for i in range(len(self.x) + 1):
            for j in range(5):
                if j == 0:
                    print("┃  " + str(data[i][j]) + " " *
                          (length - len(str(data[i][j]))), end="  ┃  ",)
                else:
                    print(str(data[i][j]).format() + " " * (length + 3 -
                                                            len(str(data[i][j]))), end="  ┃  ")
            self.printBorders(
                'mid', length) if i != len(self.x) else self.printBorders('bot', length)
        print()

    def displayCharts(self):
        ''' Method creates function and row charts. '''
        plt.figure()
        plt.plot(self.x, self.mathResults, label='Math function')
        plt.plot(self.x, self.tailorResults, label='Tailor\'s row')
        plt.annotate(self.tailor.getAdditionalParams(),
                     (median(self.x) + 0.1, median(self.tailorResults)))
        plt.legend()
        plt.title('Function\'s and Tailor\'s row charts')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.savefig('./task3/charts.png')
