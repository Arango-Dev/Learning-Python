def length(text):
    result = 0
    for _ in text:
        result += 1
    return result


l = length("Test text")
print(l)
