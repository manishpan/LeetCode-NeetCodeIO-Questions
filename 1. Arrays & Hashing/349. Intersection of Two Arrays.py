# Problem Statement: Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1, nums2):
        set1, set2 = set(), set()
        res = []

        for num in nums1:
            set1.add(num)
        
        for num in nums2:
            if num not in set2 and num in set1:
                res.append(num)
                set2.add(num)
        
        return res

# Test cases:
nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersection(nums1, nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersection(nums1, nums2))