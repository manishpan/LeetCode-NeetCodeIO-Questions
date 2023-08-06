#Problem Statement: Given an array of integers nums and an integer target, return indices of the two numbers such
#that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target: int):
        #Creating a hashTable
        hashTable = dict()

        # 1. Calculate the difference between target and nums[i]
        # 2. If diff already exists in hashTable we return the required the indices otherwise we add the element
        #    and its index to hashTable.(value:index)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashTable:
                return [hashTable[diff], i]
            hashTable[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))

nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))

nums = [3, 3]
target = 6
print(Solution().twoSum(nums, target))