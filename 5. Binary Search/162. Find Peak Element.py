#Problem Statement: A peak element is an element that is strictly greater than its neighbors.

#Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple
#peaks, return the index to any of the peaks.

#You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly 
#greater than a neighbor that is outside the array.

#You must write an algorithm that runs in O(log n) time.

class Solution:
    def findPeakElement(self, nums) -> int:
    #We intialize two pointers L and R. We calculate mid and compare it with previous element. If it is less than
    #  previous we change R pointer. Similarly for L we check it with next element.
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + ((R - L) // 2)

            if mid > 0 and nums[mid] < nums[mid-1]:
                R = mid - 1
            elif mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                L = mid + 1
            return mid

#Testcases:
nums = [1,2,3,1]
print(Solution().findPeakElement(nums))

nums = [1,2,1,3,5,6,4]
print(Solution().findPeakElement(nums))