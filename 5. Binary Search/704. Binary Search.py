#Problem Statement: Given an array of integers nums which is sorted in ascending order, and an integer target,
#write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums, target: int) -> int:
    #We create two pointers that point to start and end of nums.
        low, high = 0, len(nums) - 1

    #While low <= high, we calculate and do comparison of middle value with its target value. We changes low or high
    #accordingly, in doing so we have eliminated half of the nums.
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
    
    #If the above loop terminates normally, that means we have not found target value, so we return -1
        return -1

#Testcases:
nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target))

nums = [-1,0,3,5,9,12]
target = 2
print(Solution().search(nums, target))