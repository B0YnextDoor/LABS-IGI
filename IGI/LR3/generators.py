import random
import string


def int_sequence(size: int) -> list[int]:
    ''' Function for generating int sequence of arbitrary size\
Numbers are generated in the interval [-150, 150]. '''
    return [random.randint(-150, 150) for i in range(size)]


def literal_sequence(size: int) -> str:
    '''  Function for generating string of arbitrary size\
Using all printable ASCII characters. '''
    return ''.join(random.choices(string.printable, k=size))


def float_sequence(size: int) -> list[float]:
    ''' Function for generating float sequence of arbitrary size\
Numbers are generated in the interval [-10, 10] with 2 decimal places. '''
    return [float(format(random.uniform(-10, 10), '.2f')) for i in range(size)]
