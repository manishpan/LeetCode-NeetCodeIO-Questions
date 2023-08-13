#Problem statement: Given an integer array nums, move all 0's to the end of it while maintaining the relative order
#of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        #We create L = 0 that will point to zero. If nums[R] != 0 we swap nums[L] and nums[R].
        L = 0

        for R in range(len(nums)):
            if nums[R] != 0:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
        
        return nums

#Testcases:
nums = [0,1,0,3,12]
print(Solution().moveZeroes(nums))

nums = [0]
print(Solution().moveZeroes(nums))