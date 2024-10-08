# Problem Statement: An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

class Solution:
    def isMonotonic(self, nums):
    # We create two flags increase and decrease and initialize them with True. We then traverse the nums array and if we find that at any element, we are violating the increase or decrease property, we make the relevant flag as False. At last we do return or operation between increase and decrease.
        increase, decrease = True, True

        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                increase = False
            if nums[i] < nums[i+1]:
                decrease = False
    
        return increase or decrease
    

# Test Cases:
nums = [1,3,2]
print(Solution().isMonotonic(nums))

nums = [6,5,4,4]
print(Solution().isMonotonic(nums))

nums = [1,2,2,3]
print(Solution().isMonotonic(nums))