try:
    # context manager
    with open("input.txt", "w") as fh:
        fh.write("The quick brown fox jumps over the lazy dog\n")
except Exception as e:
    print(e)

try:
    with open("input.txt", "r") as fh:
        data = fh.read()
        print(data)
except Exception as e:
    print(e)

try:
    with open("input.txt", "a") as fh:
        fh.write("The quick brown fox jumps over the tired dog\n")
except Exception as e:
    print(e)
