def is_palindrome(text):
    toevaluate = trimwhitespaces(text)
    return toevaluate == reverseString(toevaluate)


def trimwhitespaces(text):
    toReturn = ""
    for char in text:
        if char != " ":
            toReturn += char
    return toReturn.lower()


def reverseString(text):
    return text[::-1].lower()


VARSTR = "tsetse"
print(VARSTR, is_palindrome(VARSTR))
