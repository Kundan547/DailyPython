def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    
    while low <= high:
        mid = (high + low) // 2
        
        if arr[mid] < x:
            low = mid + 1
            
        elif arr[mid] > x:
            high = mid - 1
            
        else:
            return mid
        
    return -1

arr = [2,3,4,8,54,98,12]
x = int(input("Enter the desired element: "))


result = binary_search(arr, x)

if result != -1:
    print("Element is present  at index :", str(result))
else:
    print("Element is not present in array")