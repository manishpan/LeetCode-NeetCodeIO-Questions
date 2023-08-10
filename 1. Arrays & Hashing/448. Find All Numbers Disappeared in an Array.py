#Problem statement: Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all
#the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums):
    #Mark if a value exists or not from [1,n]. If a value exists, we mark it as negative. Negative sign shows that
    #the value exists in the array.
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        result = []
    #If a value at an index is positive, that means the value i+1 does not exists in given array. So we append it at
    #result.
        for i, n in enumerate(nums):
            if n > 0:
                result.append(i + 1)
        
        return result

#Testcases:
nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))

nums = [1,1]
print(Solution().findDisappearedNumbers(nums))