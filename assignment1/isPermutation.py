def isPermutation(str1, str2):
    if str1 is None or str2 is None:
        return False
    str1 = str1.lower()
    str2 = str2.lower()
    if str1 == str2:
        return True
    allSymbols = dict()
    for symb in str1:
        allSymbols[symb] = allSymbols.get(symb, 0) + 1
    for symb in str2:
        if symb not in allSymbols.keys():
            return False
        allSymbols[symb] -= 1
    for symb in allSymbols:
        if allSymbols[symb]:
            return False
    return True

def _test():
    while True:
        print("\ninput two string")
        s1 = input()
        s2 = input()
        print(isPermutation(s1, s2))

if __name__ == "__main__":
    _test()
