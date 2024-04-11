import numpy as np


def matrixGenerator(rows: int, columns: int):
    return np.random.randint(-150, 150, size=(rows, columns))
