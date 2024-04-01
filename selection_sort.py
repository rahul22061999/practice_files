def sort(nums):
    for i in range(len(nums)):
        minpos = i 
        for j in range(i, len(nums)):  
            if nums[j] < nums[minpos]:
                minpos = j

        # Swap elements at indices i and minpos
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [7,5,9,6]
sort(nums)
print(nums)
