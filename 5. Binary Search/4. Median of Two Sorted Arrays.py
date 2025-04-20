# # Problem statement: Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        start, end = 0, len(A) - 1
        while True:
            i = (start + end) >> 1
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                #even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # Left has more elementsL
            elif Aleft > Bright:
                end = i - 1
            # Left has less elements
            else:
                start = i + 1

# Test cases:
nums1 = [1,3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [1,2]
nums2 = [3,4]
print(Solution().findMedianSortedArrays(nums1, nums2))