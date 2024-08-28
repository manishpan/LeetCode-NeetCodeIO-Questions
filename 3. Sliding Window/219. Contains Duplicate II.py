#Problem Statement: Given an integer array nums and an integer k, return true if there are two distinct indices
#i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
    
    
#Testcases:
nums = [1,2,3,1]
k = 3
print(Solution().containsNearbyDuplicate(nums, k))

nums = [1,0,1,1]
k = 1
print(Solution().containsNearbyDuplicate(nums, k))

nums = [1,2,3,1,2,3]
k = 2
print(Solution().containsNearbyDuplicate(nums, k))