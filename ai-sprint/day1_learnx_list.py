# Learning about Python lists
# A list stores ordered, mutable items.
# Review this file later to remember list methods, slicing, and how copies behave.

li = []
other_li = [4, 5, 6]

# Add items to the end of the list
li.append(1)
li.append(2)
li.append(4)
li.append(3)
print("Initial list:", li)

# Remove the last item
li.pop()
print("After pop:", li)

# Add an item back
li.append(3)
print("After re-adding 3:", li)

# Uncomment to see an index error for out-of-range access
# print(li[4])

# Slicing: li[start:end:step] - start included, end excluded
print("Slice [1:3]:", li[1:3])
print("Slice [1:-3]:", li[1:-3])
print("Slice [2:]:", li[2:])
print("Slice [:3]:", li[:3])
print("Slice [::2]:", li[::2])
print("Reverse slice [::-1]:", li[::-1])

# Copy a list and check whether it is a new object
li2 = li[:]  # Shallow copy
print("li2 is li:", li2 is li)

# Remove items by index and by value
del li[2]  # remove by index
print("After deleting index 2:", li)

li.remove(2)  # remove first matching value
print("After removing value 2:", li)

# Insert an item at a specific index
li.insert(1, 2)
print("After inserting 2 at index 1:", li)

# Find the position of a value
print("Index of 2:", li.index(2))

# Concatenate and extend the list
print("Concatenated list:", li + other_li)
print("Current list before extend:", li)

li.extend(other_li)
print("After extending with other_li:", li)

# Membership and length checks
print("Is 4 in the list?", 4 in li)
print("Length of the list:", len(li))
