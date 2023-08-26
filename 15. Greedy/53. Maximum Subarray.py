#Problem Statement: Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums) -> int:
    #We use Kadane`s algorithm to solve this problem. Basically calculating current sum and comparing each sum time
    # with maxSum.`
        maxSum = nums[0]
        curSum = 0

        for i in nums:
            curSum = max(curSum, 0) + i
            maxSum = max(curSum, maxSum)
            
        return maxSum

#Testcases:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))

nums = [1]
print(Solution().maxSubArray(nums))

nums = [5,4,-1,7,8]
print(Solution().maxSubArray(nums))