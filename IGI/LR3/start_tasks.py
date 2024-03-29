import task1
import task2
import task3
import task4
import task5
from utils import stopFunction, validateSequenceSize
from decorators import task1Decorator, chooseInputType
from generators import int_sequence, literal_sequence, float_sequence


@task1Decorator
def start_task1() -> None:
    ''' A program for calculating the value of a function using a Tailor's row of the function
with a given accuracy. '''

    while True:
        eps, x = task1.validateInput()
        if eps == 0:
            break
        task1.displayResult(x, eps)
        if stopFunction() != "0":
            print()
            continue
        break
    print('Task exit\n')


@chooseInputType
def start_task2(inputType: int) -> None:
    ''' Program for finding the sum of a sequence of integer numbers and minimal number. '''

    if (inputType == 1):
        print('Filling an array (0 -> stop enter):')
        inputArray = task2.validateInput()
    else:
        inputArray = list(int_sequence(validateSequenceSize('sequence')))
    task2.displayResults(inputArray)


@chooseInputType
def start_task3(inputType: int) -> None:
    ''' Program for analyzing text entered from the keyboard: counts the number of capital vowels. '''

    if (inputType == 1):
        inputText = input('Input your string. (Type `stop` to exit): ')
    else:
        inputText = literal_sequence(validateSequenceSize('string'))
    if inputText.lower() == 'stop':
        return 'stop'
    task3.displayResult(inputText)


def start_task4() -> None:
    ''' Program for parsing a string initialized in program code:\na) determine the number of words in a line;\n\
b) find the longest word and its serial number;\nc) print every odd word '''
    task4.analiseString()
    print('Task exit\n')


@chooseInputType
def start_task5(inputType: int) -> None:
    ''' Program for processing real lists:\nthe number of list elements lying in the range from A to B (parameters A\
and B are entered from the keyboard by the user)\nand the sum of the list elements located after the maximum element '''

    if (inputType == 1):
        collection = task5.validateInputArray()
    else:
        collection = list(float_sequence(validateSequenceSize('sequence')))
    if collection is None:
        return 'stop'
    task5.analiseCollection(collection)
