#Problem statement: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
#The order of the elements may be changed. Then return the number of elements in nums which are not equal to val

def removeElement(nums, val):
    loc = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[loc] = nums[i]
            loc += 1
    return loc

nums = [0,1,2,2,3,0,4,2]
val = 2
k = removeElement(nums, val)
print(nums[:k])