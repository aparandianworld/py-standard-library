sample_str = "The quick brown fox jumps over the lazy dog on 3rd of December 2025."

print(sample_str.lower())
print(sample_str.upper())

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
print(", ".join(letters))

result = sample_str.split(" ")
print(result)

names = ["John", "Jane", "David", "Alice", "Bob"]
longest_name = max(len(name) for name in names)

# left, center and right justification
for name in names:
    print(name.ljust(longest_name + 2, "-") + ":")

for name in names:
    print(name.rjust(longest_name + 2, "-") + ":")

for name in names:
    print(name.center(longest_name + 2, "-") + ":")

# translation table
translation_table = str.maketrans("abg", "461")
print(sample_str.translate(translation_table))
