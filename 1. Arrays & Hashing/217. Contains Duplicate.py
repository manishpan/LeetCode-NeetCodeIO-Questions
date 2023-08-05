#Problem statement: Given an integer array nums, return true if any value appears at least twice in the array, and
#return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashSet = set()

        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False

nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(nums))
