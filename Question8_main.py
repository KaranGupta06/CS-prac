import Question8_backend as backend

func_list = {
    1 : backend.generate_factors,
    2 : backend.isPrimeNo,
    3 : backend.isPerfectNo,
}

while True:
    print(*[f"| {i} | {j.__name__}" for i, j in func_list.items()], sep="\n")
    print(func_list[int(input(">>> "))](int(input("Number: "))))
    
    if input("Exit? (y/n)") == "y":
        break
    