import random
import string

moves = ["rock", "paper", "scissors"]

# method 1
for move in moves:
    i = random.randint(0, len(moves) - 1)
    random_move = moves[i]
    print(i, random_move)

# method 2 w/ choice
for move in range(len(moves)):
    print(move, random.choice(moves))

# choices method to get a list of random items
roulette_wheel = ["black", "red", "green"]
weights = [18, 18, 2]
for i in range(len(roulette_wheel)):
    print(f"list {i}: ", random.choices(roulette_wheel, weights=weights, k=10))

# sample method to get a list of random items without replacement
letters = string.ascii_letters
for i in range(10):
    print(random.sample(letters, k = 5))

# shuffle method to shuffle a list in place
players = [
    "John",
    "Mike",
    "Aaron",
    "Tom",
    "Mariah",
    "Anne"
]
print("original: ", players)
random.shuffle(players)
print("shuffled (list): ", players)

# NOTE: shuffle does not work on immutable sequences (i.e strings)
letters = random.sample(string.ascii_letters, k = 10)
print("original: ", letters)
random.shuffle(letters)
print("shuffled (string): ", letters)