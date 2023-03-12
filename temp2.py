


array = [1, 2, 3, 4, 5, 6]
print(array, id(array))

# get left
for i in range(3, len(array)):
    array[i - 1] = array[i]

print(array, id(array))

print(array[-1:])




