# Problem Statement: Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

#answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
#answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
#Note that the integers in the lists may be returned in any order.

class Solution:
    def findDifference(self, nums1, nums2):
        A_not_B, B_not_A = set(), set()
        tmpA, tmpB = set(), set()

        for num in nums1:
            tmpA.add(num)
        for num in nums2:
            if num not in tmpA:
                B_not_A.add(num)
            tmpB.add(num)
        
        for num in nums1:
            if num not in tmpB:
                A_not_B.add(num)
        
        return [list(A_not_B), list(B_not_A)]

# Test cases:
nums1 = [1,2,3]
nums2 = [2,4,6]
print(Solution().findDifference(nums1, nums2))

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(Solution().findDifference(nums1, nums2))