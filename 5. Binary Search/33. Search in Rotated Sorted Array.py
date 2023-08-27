#Problem Statement: There is an integer array nums sorted in ascending order (with distinct values).

#Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
#such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
#For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

#Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
#or -1 if it is not in nums.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums, target) -> int:
    #We initialize two pointers L, R with 0 , last index. We calculate middle of array and check whether middle
    # lies in left sorted part or right sorted part. Once, we determine the part where we are, we check whether our
    # target lies in the half where we are or in other half and changes L or R accordingly.
        L, R = 0, len(nums)-1

        while L <= R:
            mid = L + ((R - L) // 2)

            if nums[mid] == target:
                return mid
            #Middle in left sorted part.
            if nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            #Middle in right sorted part
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
        
        return -1

#Testcases:
nums = [4,5,6,7,0,1,2]
target = 0
print(Solution().search(nums, target))

nums = [4,5,6,7,0,1,2]
target = 3
print(Solution().search(nums, target))

nums = [1]
target = 0
print(Solution().search(nums, target))