import random

# 0 and 1 with uniform distribution
print(random.random())

heads = 0
tails = 0
for i in range(10):
    if random.random() <= 0.5:
        heads += 1
    else:
        tails += 1

print("heads: ", heads, "tails: ", tails)

# uniform exclude upper bound
print(random.uniform(1, 100))

# random integers (whole numbers) include upper bound
print(random.randint(1, 100))

# random integers (whole numbers) exclude upper bound
print(random.randrange(50, 100, 5))

print("---")

# Use the seed function to position the generator for predictable results
random.seed(42)
print(random.random())
print(random.random())

print("---")
random.seed(42)
print(random.random())
print(random.random())