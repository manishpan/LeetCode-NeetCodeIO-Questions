#Problem Statement: Given a non-empty array of integers nums, every element appears twice except for one. Find that
#single one.

#You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums) -> int:
    #We use the fact that x xor x = 0 and xor operation is associative. We xor each element one by one. Since, it is
    # given that every element except one appears twice, at the end xor operation will return the element that has
    # odd frequency.
        res = 0
        for i in nums:
            res = res ^ i
        return res

#Testcases:
nums = [2,2,1]
print(Solution().singleNumber(nums))

nums = [4,1,2,1,2]
print(Solution().singleNumber(nums))

nums = [1]
print(Solution().singleNumber(nums))