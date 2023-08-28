#Problem Statement: You are given a sorted array consisting of only integers where every element appears exactly 
#twice, except for one element which appears exactly once.

#Return the single element that appears only once.

#Your solution must run in O(log n) time and O(1) space.

class Solution:
    def singleNonDuplicate(self, nums) -> int:
    #We initialize two pointers L and R, calculate mid and check if it is different from both left and right element
    # if it is, we return True otherwise we have to decide whether we should go left or right. The element with
    # single appearance will be at the subarray whose length is odd. So, we calculate length of left subarray and
    # checks if it is odd. 
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + ((R - L) // 2)

            if (mid-1 < 0 or nums[mid] != nums[mid-1]) and (mid+1 == len(nums) or nums[mid] != nums[mid+1]):
                return nums[mid]
            leftSize = mid-1 if nums[mid-1] == nums[mid] else mid
            if leftSize & 1:
                R = mid - 1
            else:
                L = mid + 1

#Testcases:
nums = [1,1,2,3,3,4,4,8,8]
print(Solution().singleNonDuplicate(nums))

nums = [3,3,7,7,10,11,11]
print(Solution().singleNonDuplicate(nums))

nums = [1]
print(Solution().singleNonDuplicate(nums))