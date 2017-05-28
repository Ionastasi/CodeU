def isPermutation(str1, str2):
    """Function that checks if one string is a permutation of the other.

    Args:
        str1: first string;
        str2: second string.

    Return:
        a bool, True if the first string is a permutation of the other,
        and False otherwise.
    """
    if str1 is None or str2 is None:
        return False
    str1 = str1.lower()
    str2 = str2.lower()
    if str1 == str2:
        return True
    symbolsFromStr1 = dict()
    for symbol in str1:
        symbolsFromStr1[symbol] = symbolsFromStr1.get(symbol, 0) + 1
    for symbol in str2:
        if symbol not in symbolsFromStr1:
            return False
        symbolsFromStr1[symbol] -= 1
    for symbol in symbolsFromStr1:
        if symbolsFromStr1[symbol]:
            return False
    return True

if __name__ == "__main__":
    s1 = input("Input two string:\n>")
    s2 = input(">")
    if isPermutation(s1, s2):
        print("This two strings are a permutation of each other.")
    else:
        print("This two strings are NOT a permutation of each other.")
