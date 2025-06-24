arr = [10, 20, 30, 40, 50]
print("Original array:", arr)
del arr[0]
print("deleting at beginning:", arr)
del arr[2]
print("deleting at specific index / middle:", arr)
arr.pop()
print("deleting at end:", arr)
