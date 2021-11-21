

def compressLZ78(text):
    dictionary = dict()
    i = 0
    index = 1
    encodedNumbers = []
    encodedLetters = []
    while i < len(text):
        stringToBeSaved = text[i]
        indexInDictionary = 0
        while stringToBeSaved in dictionary:
            indexInDictionary = dictionary[stringToBeSaved]
            if (i == len(text) - 1):
                stringToBeSaved = " "
                break
            i = i + 1
            stringToBeSaved = stringToBeSaved + text[i]
        encodedNumbers.append(indexInDictionary)
        encodedLetters.append(stringToBeSaved[len(stringToBeSaved) - 1])
        if (stringToBeSaved not in dictionary):
            dictionary[stringToBeSaved] = index
            index = index + 1
        i = i + 1

    return encodedNumbers, encodedLetters, dictionary


def decompressLZ78(encodedNumbers, encodedLetters, dictionary):
    l = []
    i = 0
    while i < len(encodedNumbers):
        if (encodedNumbers[i] != 0):
            l.append(list(dictionary.keys())[
                     list(dictionary.values()).index(encodedNumbers[i])])
        l.append(encodedLetters[i])
        i = i+1
    return l


def test():
    # How to use:
    encodedNumbers, encodedLetters, dictionary = compressLZ78(
        'wabba wabba wabba wabba woo woo woo')
    #encodedNumbers, encodedLetters, dictionary = compressLZ78('pipapipapipo')
    print("enc numbers: "+str(encodedNumbers))
    print("enc letters: "+str(encodedLetters))
    print("dict: "+str(dictionary))
    decompressed = decompressLZ78(
        encodedNumbers, encodedLetters, dictionary)

    decoded = ""
    for c in decompressed:
        decoded += c
    print(decoded)
