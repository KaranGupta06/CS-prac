def roman_to_integer(num):
    conv = {
        "I" : 1, "X" : 10, "C" : 100,
        "V" : 5, "L" : 50, "D" : 500, "M" : 1000
        }
    
    integer = 0
    
    for i in range(len(num)):
        if i != len(num) - 1 and conv[num[i + 1]] > conv[num[i]]:
            integer -= 2*conv[num[i]]
        integer += conv[num[i]]

    return integer

print(roman_to_integer(input(">>> ")))