import os

FILE_PATH = r"C:\Users\Admin\Desktop\Karan\PYTHON\School Project\Practical File\Files\file.txt"

def file_write():

    text = """Neither apple nor pine are in pineapple. Boxing rings are square.
Writers write, but fingers don't fing. Overlook and oversee are opposites.
A house can burn up as it burns down. An alarm goes off by going on."""
    
    with open(FILE_PATH, "w") as f:
        f.write(text)

def file_read():
    with open(FILE_PATH, "r") as f:
        print(f.read())

def file_append():
    with open(FILE_PATH, "a+") as f:
        f.write("\nPink Floyd is a great band.")
        f.seek(0)
        
        for i, line in enumerate(f.readlines()):
            print(i+1, line.strip("\n"))

def file_display_end():
    with open(FILE_PATH, "r") as f:
        print(f.readlines()[-1])

def file_display_first_n():
    with open(FILE_PATH, "r") as f:
        print(f.readline()[10:].strip("\n"))

def file_display_line(line_number=None):
    line_number = line_number if line_number else int(input("Line: "))
    with open(FILE_PATH, "r") as f:
        print(f.readlines()[line_number - 1].strip("\n"))

def file_freq():

    with open(FILE_PATH, "r") as f:
        text = " ".join(f.read().split("\n")).split()

    freq_dict = {
        chr(97 + i): sum([1 for j in text if j[0].lower() == chr(97 + i)]) for i in range(26)
    }

    for key, value in freq_dict.items():
        print(f"Words beginning with '{key}' : {value}")

for func in [file_write, file_read, file_append, file_display_end,
             file_display_first_n, file_display_line, file_freq]:
    print(func.__name__.center(os.get_terminal_size().columns, "-"))
    func()