import array
#static array
# Create an integer array
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr[1]) 


#Using Lists
# Can store different data types
# Dynamic in size
# Commonly used in place of arrays
numbers = [10, 20, 30, 40, 50]
print(numbers[0])


# 1) append(x) – Add element to end
numbers.append(50)
print("After append(60)):", numbers)

#2) insert(i, x) – Insert at index
numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

#3)remove(x) – Remove first occurrence
numbers.remove(30)
print("After remove(30):", numbers)
#4)pop([i]) – Remove and return item by index
item = numbers.pop(3)
print("After pop(3):", numbers)
print("Popped item:", item)
#5)index(x) – Get index of value
idex = numbers.index(25)
print("Index of 25:", idex)
#6)sort() – Sort the list
numbers.sort()
print("After sort():", numbers)
#7)reverse() – Reverse the list
numbers.reverse()
print("After reverse():", numbers)
#8)copy() – Copy the list
arr_1 = [1, 2, 3]
arr_copy = arr_1.copy()
print("Original:", arr_1)
print("Copy:", arr_copy)
#==============
print("Number array:", numbers)
#9)count(x) – Count occurrences of value
count = numbers.count(50)
print("Count of 50:", count)
#fixed size array
# Create an empty list with 10 elements initialized to 0
vijay = [0] *2
print("Empty list with 10 elements:", vijay)
vijay[1]=2
print("Updated list:", vijay)
#vijay[2]=4
#print("Updated list:", vijay)   #index out of range

#===================
import array

fix_arr = array.array('i', [0]*5)  # Fixed size array of 5 integers initialized to 0
print(fix_arr)
fix_arr.append(10)  # Append an element
print("After append(10):", fix_arr)