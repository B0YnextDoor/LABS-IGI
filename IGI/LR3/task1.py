from math import log
from utils import validateNumberInput


def validateInput() -> tuple[float, float]:
    ''' Function for validation input of accuracy and x value. '''
    eps = validateNumberInput(
        'accuracy (0 < acc < 1) (0 -> Exit function)', '0 < acc < 1', float, condition=lambda x: x < 0 or x >= 1)
    if eps == 0:
        return eps, 0
    x = validateNumberInput(
        'x (|x| > 1)', '|x| must be bigger than 1', float, condition=lambda x: abs(x) <= 1)
    return eps, x


def countTailor(x: float, eps: float, mathResult: float) -> tuple[float, int]:
    ''' Function that counts sum of Tailor's row with the required accuracy. '''
    tailorSum = 0
    N = -1
    while N + 1 < 500:
        N += 1
        tailorSum += 1/((2*N+1)*x**(2*N+1))
        if (abs(2*tailorSum - mathResult) >= eps/10):
            continue
        break
    return 2*tailorSum, N+1


def printBorders(type: str, length: int) -> None:
    ''' Functions prints result table borders. '''
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


def displayResult(x: float, eps: float) -> None:
    ''' Function displays th result. '''
    mathResult = log((x+1)/(x-1))
    tailorSum, iterations = countTailor(x, eps, mathResult)
    length = max(len(str(tailorSum)), len(str(iterations)),
                 len((str(eps))), len(str(x)), 9)
    data = [["x", "n", "F(x)", "Math F(x)", "eps"], [
        x, iterations, round(tailorSum, len(str(eps))), round(mathResult, len(str(eps))), eps]]
    printBorders('top', length)
    for i in range(2):
        for j in range(5):
            if j == 0:
                print("┃  " + str(data[i][j]) + " " *
                      (length - len(str(data[i][j]))), end="  ┃  ",)
            else:
                print(str(data[i][j]).format() + " " * (length + 3 -
                      len(str(data[i][j]))), end="  ┃  ")
        printBorders('mid', length) if i != 1 else printBorders('bot', length)
