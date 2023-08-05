#Problem Statement: Given an integer array nums of length n, you want to create an array ans of length 2n where
#ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

#Specifically, ans is the concatenation of two nums arrays.

#Return the array ans.

class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
    
    #Creating a new array ans filled with 0 and length = 2n.
        ans = [0] * 2 * n
    
    #Updating ans as per requirements
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans

nums = [1,2,1]
print(Solution().getConcatenation(nums)) 