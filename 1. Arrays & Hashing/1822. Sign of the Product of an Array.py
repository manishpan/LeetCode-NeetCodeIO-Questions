#Problem Statement: There is a function signFunc(x) that returns:

#1 if x is positive.
#-1 if x is negative.
#0 if x is equal to 0.
#You are given an integer array nums. Let product be the product of all values in the array nums.

#Return signFunc(product).

class Solution:
    def arraySign(self, nums) -> int:
    #We create a variable that will be used to store the sign of product. If we encounter a negative value, we flip
    # the sign to negative. Again, if we encounter a negative value we flip the sign making it positive again.
        sign = 1
    
    #If current element is 0, then product is 0 so we return 0 immediately. Otherwise, we flip the sign if we
    # encounter a negative value.
        for i in nums:
            if i == 0:  return 0
            elif i < 0: sign = -1 * sign

        return sign

#Testcase:
nums = [-1,-2,-3,-4,3,2,1]
print(Solution().arraySign(nums))

nums = [1,5,0,2,-3]
print(Solution().arraySign(nums))

nums = [-1,1,-1,1,-1]
print(Solution().arraySign(nums))