def search(arr, x):
    # Ensure arr supports length; convert iterables or wrap scalars
    if not hasattr(arr, '__len__'):
        if hasattr(arr, '__iter__'):
            arr = list(arr)
        else:
            arr = [arr]
    n = len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == x:
                return i, j 
    return None 
if __name__ == "__main__":
    user_choice = input("Enter the array (space-separated): ")
    arr = [int(num) for num in user_choice.split()]
    x = int(input("Enter number to search: "))
    result = search(arr, x)
    if result:
        print(f"Elements found at indices: {result}")
    else:
        print("No two numbers add up to the target.")