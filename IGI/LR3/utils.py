def stopFunction() -> str:
    ''' Function stops running task. '''
    return input('Do you want to continue? (0 -> No | anything else -> Yes): ')


def validateNumberInput(inputMessage: str, errorMessage: str, numberType, condition=lambda x: type(x) == str) -> int:
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


def validateSequenceSize(name: str) -> int:
    ''' Function validates input of size of sequence. '''
    return validateNumberInput(
        f'size of {name}', 'size > 0', int, condition=lambda x: x <= 0)
