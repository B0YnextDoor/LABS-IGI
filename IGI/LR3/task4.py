initialString = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."


def clearString() -> list[str]:
    ''' Function converts a string to replace all non-letter characters with spaces. '''
    clearString = "".join(
        el for el in initialString if el.isalpha() or el == ' ' or el == '-')
    return clearString.split(' ')


def findMaxLenWord(words: list[str]) -> None:
    ''' Function finds max len word and its position in the string. '''
    maxLenWords: list[tuple[int, str]] = [(0, '')]
    for id, word in enumerate(words):
        if len(word) > len(maxLenWords[0][1]):
            maxLenWords.clear()
            maxLenWords.append((id, word))
        elif len(word) == len(maxLenWords[0][1]):
            maxLenWords.append((id, word))
    print(
        f"Max length word{'s' if len(maxLenWords) > 1 else '' } => Max length: {len(maxLenWords[0][1])}:")
    for id, word in maxLenWords:
        print(f'{word} -> Position: {id}')
    print()


def displayOddWords(words: list[str]) -> None:
    ''' Function prints odd words of the string. '''
    print('Odd words:')
    for i in range(0, len(words), 2):
        print(words[i], end=" ")


def analiseString() -> None:
    ''' Function analises string and displays results. '''
    print('Initial string:')
    print(initialString)
    print("\nAnalised string:")
    words = clearString()
    print(f'Ammount of words: {len(words)}\n')
    findMaxLenWord(words)
    displayOddWords(words)
    print('Task exit\n')
