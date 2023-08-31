import csv

data = []

with open("placement.csv", "r") as f:
    for line in csv.reader(f):
        data.append(line.split(","))

def no_of_test_givers():
    return len(data)

def top_n_scorers(n):
    return sorted(data, lambda x: x[2]+x[3]+x[4]+x[5]+x[6])[n:]

