#deletion at beginning
arr = [10, 20, 30, 40]
print("Array before deletion")
for i in range(len(arr)):
    print(arr[i], end=" ")
del arr[0]
print("\nArray after deletion")
for i in range(len(arr)):
    print(arr[i], end=" ")
    
#deletion at position
arr = [10, 20, 30, 40]
pos = 2
print("Array before deletion")
for num in arr:
    print(num, end=" ")
del arr[pos - 1]
print("\nArray after deletion")
for num in arr:
    print(num, end=" ")
    
#deletion at first occurrence
arr = [10, 20, 20, 20, 30]
ele = 20
print("Array before deletion")
for num in arr:
		print(num, end=" ")
if ele in arr:
	arr.remove(ele)
print("\nArray after deletion")
for num in arr:
	print(num, end=" ")
 
#deletion at all occurrence
from typing import List
def remove_element(arr: List[int], ele: int) -> int:
    k = 0
    for i in range(len(arr)):
        if arr[i]!= ele:
            arr[k], arr[i] = arr[i], arr[k]
            k += 1
    return k
def main():
    arr = [0, 1, 3, 0, 2, 2, 4, 2]
    ele = 2
    print(remove_element(arr, ele))