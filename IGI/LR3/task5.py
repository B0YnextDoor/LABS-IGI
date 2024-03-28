from utils import validateNumberInput


def validateInputArray() -> list[float]:
    ''' Function validates input of sequence and its lenght. '''
    N = validateNumberInput(
        'length of array (len > 0) (0 -> Exit function)', 'len > 0', int, condition=lambda x: x < 0)
    if N == 0:
        return None
    k = 0
    collection = list[float]()
    while k < N:
        el = validateNumberInput(
            f'#{k + 1} element (float number)', '', float)
        collection.append(el)
        k += 1
    return collection


def validateInputBorders() -> tuple[int, int]:
    ''' Function validates input of interval borders. '''
    while True:
        A = validateNumberInput('left border: ', '', int)
        B = validateNumberInput(
            'rigth border: ', '', int)
        if B < A:
            print('Wrong input -> (left border <= right border)! Try again.')
            continue
        break
    return A, B


def displayCollection(collection: list[float]) -> None:
    ''' Function displays collection. '''
    print('Entered collection:')
    for el in collection:
        print(el, end=" ")
    print()


def findAmmountInInterval(collection: list[float], A: int, B: int) -> int:
    ''' Function counts an ammount of collection elements in the interval. '''
    return sum(1 if el >= A and el <= B else 0 for el in collection)


def findMaxElement(collection: list[float]) -> tuple[int, float]:
    ''' Function finds collection max element and its position. '''
    return max(enumerate(collection), key=lambda el: el[1])


def findSumInterval(collection: list[float], start: int) -> float:
    ''' Function finds sum of elements from the `start` position to the end of collection. '''
    return sum(collection[i] for i in range(start, len(collection)))


def analiseCollection(collection: list[float]) -> str | None:
    ''' Function analises function and displays results. '''
    displayCollection(collection)
    A, B = validateInputBorders()
    print('Analised collection:')
    print(
        f'Ammount of elements in [{A}, {B}]: {findAmmountInInterval(collection, A, B)}')
    maxElement = findMaxElement(collection)
    print(f"Max element: {maxElement[1]}")
    print(
        f"Sum of elements after Max: {findSumInterval(collection, maxElement[0] + 1)}")
