
linear_arr= [1, 2, 3, 4, 5]
print("Linear Array:", linear_arr)
# traversal array using for loop
print("-----------------------------------------")
print("Using for loop:")
for items in linear_arr:
  print(items)
for i in range(len(linear_arr)):
  print("Index:", i, "Value:", linear_arr[i])

for element in linear_arr:
    print("Element:", element)

#using while loop
print("=================================================")
print("Using while loop:")
i=0
while i < len(linear_arr):
    print("Element at index", [i], "=", linear_arr[i])
    i += 1
#using index in range
#Access both index and value
print("=================================================")
print("Using index in range:")
for index in range(len(linear_arr)):
    print("Element at index", [index], "=", linear_arr[index])


print("*************************************************")
#searching in array
number = 5
# for i in range(len(linear_arr)):
#     if linear_arr[i] == number:
#         print("Element", number, "found at index", i)
#         break
#     else:
#         print("Element", number, "not found at index", i)

for element in linear_arr:
      if element == number:
          print("Element", number, "found")
          break
      else:
          print("Element", number, "not found")
print("*******************==============******************************")
arr = [10, 20, 30, 40, 50]
key = int(input("Enter the value to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print(f"{key} found at index {i}")
        found = True
        break  # Stop once found

if not found:
    print(f"{key} not found in the array.")