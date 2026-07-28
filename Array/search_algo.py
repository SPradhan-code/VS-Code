#linear search
def search(arr, x):
    n = len(arr)
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = search(arr, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
        
#linear search with user input
def search(arr, x):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1
if __name__ == "__main__":
    user_string = input("Enter numbers for the array: ")
    arr = [int(num) for num in user_string.split()]
    x = int(input("Enter number to search: "))
    result = search(arr, x)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
        
#binary search
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binarySearch(arr, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
    