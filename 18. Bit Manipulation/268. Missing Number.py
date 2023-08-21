#Problem Statement: Given an array nums containing n distinct numbers in the range [0, n], return the only number in
#the range that is missing from the array.

class Solution:
    def missingNumber(self, nums) -> int:
    #We can calculate the sum to len(nums) using first N natural numbers formula, then subtract it from the sum of
    # values in nums, to get the missing number.
        n = len(nums)
        sumToN = (n * (n+1)) // 2
        return sumToN - sum(nums)
    
    def missingNumberXOR(self, nums) -> int:
    #Since, x xor x = 0, we can calculate XOR of first N natural numbers and XOR of numbers in nums. After calculation
    # we can perform xor between these numbers to get the missing numbers.
        res1, res2 = len(nums), 0

        for i in range(res1):
            res1 = res1 ^ i
            res2 = res2 ^ nums[i]
            
        return res1 ^ res2

#Testcases:
nums = [3,0,1]
print(Solution().missingNumberXOR(nums))

nums = [0,1]
print(Solution().missingNumber(nums))

nums = [9,6,4,2,3,5,7,0,1]
print(Solution().missingNumber(nums))