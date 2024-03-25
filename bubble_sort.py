def sort(nums):
    for i in range(len(nums)-1, 0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
               
                
nums = [1,58,98,6,3,2,4,2,5,8,78,45,8,56]
sort(nums)
print(nums)