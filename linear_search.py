def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 
arr = [1,24,35,3,3,6,7,8,5,3,5,7,8,]
target = 35
result = linear_search(arr,target)
if result !=-1:
    print(f"The element {target} and found at index {result}")

else:
    print("bye")w