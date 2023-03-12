
x = [123, 33, 32453, 3, 25, 3]
print(id(x))

x.insert(0, 999)
x.insert(3, 999)
x.append(999)
x.remove(999)
x.pop(2)
x.extend([0,1,2,3])

print(id(x))
print(x)



# // Say we want to insert the element at index 2.
# // First, we will have to create space for the new element.
# for (int i = 4; i >= 2; i--)
# {
#     // Shift each element one position to the right.
#     intArray[i + 1] = intArray[i];
# }
#
# // Now that we have created space for the new element,
# // we can insert it at the required index.
# intArray[2] = 30;


