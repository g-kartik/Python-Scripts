def isIn(char, aStr):
    """
    :param char: a single character
    :param aStr: an alphabetized string
    :return: True if char is in aStr; False otherwise
    """

    if len(aStr) == 0:
        return False
    else:
        mid = len(aStr) // 2

    if aStr[mid] == char:
        return True
    elif aStr[mid] > char:
        return isIn(char, aStr[:mid])
    else:
        # remember not to include just mid index here while slicing, since it has already been tested
        # use mid + 1
        return isIn(char, aStr[mid + 1:])

# Test Cases
# print(isIn('a', ''))
# print(isIn('i', 'iqqz'))
# print(isIn('r', 'bdefoprrrswzz'))
# print(isIn('f', 'abbchjklpqqtvvzz'))
# print(isIn('j', 'bcdegkmnpqrssvvwxzz'))
print(isIn('l', 'aabbbehhjlmmmpruww'))
# print(isIn('l', 'abbcdeejlllmmnpttwwx'))
# print(isIn('d', 'adgmos'))
# print(isIn('e', 'abgijkmmnnrsuvwxz'))
# print(isIn('w', 'bdefilmppqssvwxy'))
