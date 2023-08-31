def isvowel():
    with open("file1.txt", "r") as f:
        text = " ".join(f.read().split("\n")).split()
    with open("file2.txt", "x") as f:
        f.write(" ".join([i for i in text if i[0].lower() in "aeiou"]))
