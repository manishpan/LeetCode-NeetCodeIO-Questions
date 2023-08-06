#Problem statement: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
#The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

#Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the
#following things:

#Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
#The remaining elements of nums are not important as well as the size of nums.

#Return k.

class Solution:
    def removeElement(self, nums, val: int) -> int:
    #Index will point to the value that needs to be replaced
        ind = 0

    #If ind element is not equal to val, we swap with itself otherwise i points to the first non-val element and we
    #overwrite it index
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ind] = nums[i]
                ind += 1
        
        return ind
            
#TestCases:
nums = [3,2,2,3]
val = 3
print(Solution().removeElement(nums, val))

nums = [0,1,2,2,3,0,4,2]
val = 2
print(Solution().removeElement(nums, val))