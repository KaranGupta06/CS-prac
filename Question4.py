with open("myfile.txt", "r") as f:
    data = " ".join(f.read().split("\n")).split()
    freq_dict = {word: data.count(word) for word in set(data)}

print("Total Number of words:", len(data))
print("Total Number of different words:", len(freq_dict.keys()))
print("Most common words:", sorted(list(freq_dict.items()), lambda x: x[1]))

len_dict = {
    length: [word for word in data if len(word) == data]
    for length in set([len(word) for word in data])
    }

print(len_dict)

def find_longest_word():
    return max(list(len_dict.values()), key=lambda x: x[0])[1]

def filter_long_words(n: int):
    return [word for word in data if len(word) > n]

