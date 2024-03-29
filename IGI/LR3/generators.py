import random
import string


def int_sequence(size: int):
    ''' Function for generating int sequence of arbitrary size\
Numbers are generated in the interval [-150, 150]. '''
    for i in range(size):
        yield random.randint(-150, 150)


def literal_sequence(size: int) -> str:
    '''  Function for generating string of arbitrary size\
Using all printable ASCII characters. '''
    return ''.join(random.choices(string.printable, k=size))


def float_sequence(size: int):
    ''' Function for generating float sequence of arbitrary size\
Numbers are generated in the interval [-10, 10] with 2 decimal places. '''
    for i in range(size):
        yield float(format(random.uniform(-10, 10), '.2f'))
