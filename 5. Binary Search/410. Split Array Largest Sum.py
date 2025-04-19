# Problem statement: Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

class Solution(object):
    def splitArray(self, nums, k):
        n = len(nums)
        if n < k:
            return -1

        def isValid(nums, k, mid):
            count = 1
            sum = 0

            for i in range(n):
                sum = sum + nums[i]
                if sum > mid:
                    count += 1
                    sum = nums[i]
                if count > k:
                    return False
            return True
        
        start, end = max(nums), sum(nums)
        res = -1

        while start <= end:
            mid = start + ((end - start) >> 1)

            if isValid(nums, k, mid):
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return res


# Test cases:
nums = [7,2,5,10,8]
k = 2
print(Solution().splitArray(nums, k))


nums = [1,2,3,4,5]
k = 2
print(Solution().splitArray(nums, k))