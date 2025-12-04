from array import array

numbers = list(range(10))
numbers_array = array("i", numbers)

print("original numbers:", numbers_array)
print("type code: ", numbers_array.typecode)

numbers_array[0] = -100
numbers_array.append(-999)
numbers_array.insert(10, -998)
numbers_array.extend([24, 25, 26])

print("updated numbers:", numbers_array)

for index, value in enumerate(numbers_array):
    numbers_array[index] = value * 2

print("doubled numbers:", numbers_array)

# back to list (all restrictions removed...)
numbers_list = numbers_array.tolist()
print("numbers list:", numbers_list)
