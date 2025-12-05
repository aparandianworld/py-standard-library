def safe_file_operation(filename, mode, operation):
    try:
        with open(filename, mode) as fh:
            return operation(fh)
    except Exception as e:
        print(e)

# write
safe_file_operation("./input_2.txt", "w", lambda fh: fh.write("The quick brown fox jumps over the lazy dog\n"))

# read
data = safe_file_operation("./input_2.txt", "r", lambda fh: fh.read())
if data:
    print(data)

# append
safe_file_operation("./input_2.txt", "a", lambda fh: fh.write("The quick brown fox jumps over the tired dog\n"))