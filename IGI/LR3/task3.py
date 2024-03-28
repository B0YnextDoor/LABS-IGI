def reformString(inputText: str) -> str:
    terminators = ['\n', '\r', '\t', '\0', '\x0a',
                   '\x0b', '\x0c', '\x0d', '\x08', '\x09', '\x1b']
    for el in terminators:
        inputText = inputText.replace(el, ' ')
    return inputText


def countInputVowels(inputText: str) -> tuple[dict[str, int], dict[str, list[int]]]:
    ''' Function counts ammout of each vowel and their positions in the input string. '''
    vowels = ['A', 'E', 'I', 'O', 'U']
    countVowels: dict[str, int] = dict.fromkeys(vowels, 0)
    positions: dict[str, list[int]] = {v: list() for v in vowels}
    for i in range(len(inputText)):
        if inputText[i] in vowels:
            countVowels[inputText[i]] += 1
            positions[inputText[i]].append(i)
    return countVowels, positions


def displayPositions(inputText: str, positions: list[int]) -> None:
    ''' Function displays the positions of vowel in the string. '''
    if len(positions) == 0:
        print('No references\n')
        return
    print(inputText)
    for i in range(len(inputText)):
        if i not in positions:
            print(' ', end='')
            continue
        print('*', end='')
        positions.remove(i)
        if len(positions) == 0:
            print()
            break


def displayResult(inputText: str) -> str | None:
    ''' Fucntion displays the result. '''
    print('Input string:')
    print(repr(inputText))
    countVowels, positions = countInputVowels(inputText)
    inputText = reformString(inputText)
    for vowel in countVowels.keys():
        print(f'Vowel: `{vowel}` -> Ammout: {countVowels[vowel]}')
        displayPositions(inputText, positions[vowel])
