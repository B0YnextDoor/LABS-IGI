from utils import stopFunction


def task1Decorator(func) -> None:
    ''' Decorator for displaying task1 info. '''
    def printInfo():
        help(func)
        print("Functiuon: ln((x+1)/(x-1))")
        print("Tailor's row: 2*sum(1/(2*n+1)*x^(2n+1), n=0..inf)\n")
        func()
    return printInfo


def chooseInputType(func) -> None:
    ''' Decorator for checking the choice between 1 and 2 (Input by keyboard or random generator) and running task. '''
    def inputType():
        help(func)
        while (True):
            while True:
                print("Enter your input type:\n1 - Keyboard\n2 - Random generator\n")
                try:
                    choice = int(input())
                    if choice != 1 and choice != 2:
                        raise Exception
                except:
                    print(
                        'Incorrect input, try again! Input only one number\n1 - Keyboard\n2 - Random generator\n')
                    continue
                break
            res = func(choice)
            if res is None and stopFunction() != "0":
                print()
                continue
            break
        print('Task exit\n')
    return inputType
