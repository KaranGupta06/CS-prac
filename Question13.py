def areEqual(str1, str2):
    return simplify(str1) == simplify(str2)

def simplify(str):
    stack = []
    for i in str:
        if i != "#":
            stack.append(i)
        else:
            stack.pop()
    return "".join(stack)

str1 = input("String 1: ")
str2 = input("String 2: ")

print(areEqual(str1, str2))
