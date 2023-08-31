import pickle

users = []

with open("hotel.dat", "rb") as f:
    while True:
        try:
            users.append(pickle.load(f))
        except EOFError:
            break

print(users)
print(len(users))
print([user for user in users if user["duration"] > 2])
