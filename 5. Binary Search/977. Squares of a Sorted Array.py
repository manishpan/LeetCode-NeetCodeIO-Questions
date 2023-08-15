#Problem Statement: Given an integer array nums sorted in non-decreasing order, return an array of the squares of
#each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums):
    #We initialize L and R to point at the beginning and ending of nums. The res array will store the squares of 
    #values in nums. We will starting filling from the end of the result.
        L, R = 0, len(nums) - 1
        res = [0] * (R - L + 1)
        i = R
        while i >= 0:
            if abs(nums[L]) < abs(nums[R]):
                res[i] = nums[R] ** 2
                R -= 1
            else:
                res[i] = nums[L] ** 2
                L += 1
            i -= 1
        
        return res

#Testcases:
nums = [-4,-1,0,3,10]
print(Solution().sortedSquares(nums))

nums = [-7,-3,2,3,11]
print(Solution().sortedSquares(nums))