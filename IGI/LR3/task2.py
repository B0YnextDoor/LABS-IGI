from utils import validateNumberInput


def validateInput() -> list[int]:
    ''' Function for validation input of sequence. '''
    collection: list[int] = list()
    while True:
        n = validateNumberInput(
            'the integer number', '', int)
        if n == 0:
            break
        collection.append(n)
        continue
    return collection


def displayResults(inputArray: list[int]) -> None:
    ''' Function analising sequence and displays results. '''
    print('Input array:')
    for i in range(len(inputArray)):
        print(f'Element #{i + 1} -> {inputArray[i]}')
    if (len(inputArray) > 0):
        print(f"\nSum of elements: {sum(inputArray)}")
        print(f"Minimal value: {min(inputArray)}")
    else:
        print('Array is empty!')
