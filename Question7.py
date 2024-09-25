num = int(input("Number: "))

def _count(n):
    return len(str(n))
def _hasdigit(n, r):
    return str(r) in str(n)
def _reverse(n):
    return int(str(n)[::-1])
def _show(n):
    return [int(n)*10**i for i, n in enumerate(str(n)[::-1])]
# easter egg
print(_count(num))
print(_hasdigit(num, int(input("Digit: "))))
print(_reverse(num))
print(_show(num))
