from matplotlib import pyplot as plt


def stopFunction(action: str = 'continue') -> str:
    ''' Function stops running task. '''
    return input(f'Do you want to {action}? (0 -> No | anything else -> Yes): ')


def validateNumberInput(inputMessage: str, errorMessage: str, numberType, condition=lambda x: type(x) == str):
    ''' Function validates input of a number with a given type and condition. '''
    while True:
        try:
            N = numberType(
                input(f'Enter {inputMessage}: '))
            if condition(N):
                print(f'Wrong input -> ({errorMessage})! Try again.\n')
                continue
        except ValueError:
            print('Wrong input! Try again.\n')
            continue
        break
    return N


def validateColorInput(figure: str) -> str:
    ''' Function validates input of figure color. '''
    while True:
        color = input(f'Input {figure} color: ')
        try:
            plt.plot([], [], color=color)
        except ValueError:
            print('Color is not available!\n')
            continue
        break
    return color
