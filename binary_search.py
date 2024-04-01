def binary_search(arr, result):
    low = 0 
    high = len(arr) -1
    while low <= high:
        mid = (low +high) //2

        if arr[mid] == target:
            return mid 
        
        elif arr[mid] < target:
            low = mid +1 
        else:
            high = mid -1
    return -1

arr = [1,2,3,4,2,1,4,35,45,3]
arr_sorted = sorted(arr)
target = 45
result = binary_search(arr_sorted,target)
if result != -1:
    print(arr_sorted)
    print(f"The value {target} is in index {result}")
else:
    print("not found")