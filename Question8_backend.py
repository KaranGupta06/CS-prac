def generate_factors(num):
    return [i for i in range(1, num) if num%i == 0]
def isPrimeNo(num):
    return len(generate_factors(num)) == 1
def isPerfectNo(num):
    return num == sum(generate_factors(num))
