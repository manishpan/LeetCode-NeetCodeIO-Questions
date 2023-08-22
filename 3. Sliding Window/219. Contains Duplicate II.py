#Problem Statement: Given an integer array nums and an integer k, return true if there are two distinct indices
#i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
    #We take a set that represents our window, two pointers L and R will mark the beginning and end of our sliding
    # window. If window size is becomes k, we remove L and increment it. In next iteration if nums[R] is already
    # in our window, that means it is a duplicate and we return True. Otherwise, we add nums[R] in our window.
        window = set()
        L, R = 0, 0

        while R < len(nums):
            if nums[R] in window:
                return True
            window.add(nums[R])

            if R - L == k:
                window.remove(nums[L])
                L += 1
            R += 1
        
        return False

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