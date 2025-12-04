sample_str = "The quick brown fox jumps over the lazy dog on 3rd of December 2025."

print(sample_str.startswith("The"))
print(sample_str.endswith("2025."))

print(sample_str.find("fox"))
print(sample_str.rfind("over"))

print("lazy" in sample_str)

# strings are immutable
example_str = sample_str.replace("lazy", "tired")
print(example_str)

print(sample_str.count("jump"))