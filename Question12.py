stack = []
temp_stack = []

while True:
    inp = int(input("Ring size: "))
    if not stack or inp >= stack[-1]:
        stack.append(inp)
    else:
        temp_stack.append(inp)
    print(stack, temp_stack)
    if input("Exit (y/n)") == "y":
        break