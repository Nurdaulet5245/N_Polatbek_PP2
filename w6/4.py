def srev(str1):

    rev = ''
    index = len(str1)
    while index > 0:
        rev += str1[ index - 1 ]
        index = index - 1
    return rev
str=input()
print(srev(str))