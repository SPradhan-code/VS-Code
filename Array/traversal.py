#linear traversal
arr = [1, 2, 3, 4, 5]
print("Linear Traversal: ", end=" ")
for i in arr:
    print(i, end=" ")
print()

#reverse traversal
arr = [1, 2, 3, 4, 5]
print("Reverse Traversal: ", end="")
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
print()

#using for loop
arr=[10,20,30,40,50]
print("Traversal using for loop: ", end="")
for i in arr:
    print(arr[i], end=" ")
print()

#using while loop
arr = [10, 20, 30, 40, 50]
n = len(arr)
i = 0
print("Traversal using while loop: ", end=" ")
while i < n:
    print(arr[i], end=" ")
    i = i+1
print()

#using foreach loop
arr = [10, 20, 30, 40, 50]
print("Traversal using foreach loop:", end=' ')
for value in arr:
    print(value, end=' ')
print()

#searching elements
arr = [10, 20, 30, 40, 50]
target = 30
found = False

# Linear search using traversal
for i in range(len(arr)):
    if arr[i] == target:
        found = True
        break
if found:
    print("Element found!")
else:
    print("Element not found!")
    
#modifying elements
arr = [10, 20, 30, 40, 50]
for i in range(len(arr)):
    arr[i] += 5
print("Modified array:", end=' ')
for num in arr:
    print(num, end=' ')
print()