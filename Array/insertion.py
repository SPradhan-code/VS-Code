#insert at beginning
arr=[20,30,40,50,60]
element=10
print("Array before insertion: ")
for i in range(len(arr)):
    print(arr[i], end=" ")  
arr.insert(0,element)
print("\nArray after insertion: ")
for i in range(len(arr)):
    print(arr[i], end=" ")
    
#insert at random place
arr=[10,20,30,50,60]
element=40
position=3
print("\nArray before insertion:")
for i in range(len(arr)):
    print(arr[i],end=" ")
arr.insert(3,40)
print("\nArray after insertion: ")
for i in range(len(arr)):
    print(arr[i], end=" ")
    
#insert at the end
arr = [10, 20, 30, 40]
ele = 50
print("Array before insertion")
for i in range(len(arr)):
        print(arr[i], end=" ")
arr.append(ele)
print("\nArray after insertion")
for i in range(len(arr)):
        print(arr[i], end=" ")