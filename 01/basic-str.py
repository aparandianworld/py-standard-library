import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.punctuation)

sample_str = "The quick brown fox jumps over the lazy dog on 3rd of December 2025."
ascii_letters = string.ascii_letters

result = "".join(c for c in sample_str if c in ascii_letters)
print(result)

print(result.isalpha())
print(result.isalnum())
print(result.isnumeric())

print(
    all(
        [
            c.isalpha() or c.isspace() or c.isdigit() or c in string.punctuation
            for c in sample_str
        ]
    )
)
