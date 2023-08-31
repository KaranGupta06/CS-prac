def convert_base(num, base):
    if num < base:
        return table[num]
    return convert_base(num//base, base) + table[num%base]

table = {0:  "0", 1:  "1", 2:  "2", 3:  "3",
         4:  "4", 5:  "5", 6:  "6", 7:  "7",
         8:  "8", 9:  "9", 10: "a", 11: "b",
         12: "c", 13: "d", 14: "e", 15: "f"}

num  = int(input("Enter an integer number: "))
base = input("Enter a base (B/O/X): ").lower()

base_num = 2 if base == "b" else (8 if base == "o" else 16)
sign = '-' if num < 0 else ''

print(f">>> {sign}0{base}{convert_base(abs(num), base_num)}")
