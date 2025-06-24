arr = [100, 200, 300]

print("Reverse traversal using reversed():")
for value in reversed(arr):
    index = arr.index(value)  # Get the first index of the value
    print([index],"=",value)
