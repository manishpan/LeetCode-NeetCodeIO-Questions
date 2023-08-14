#Problem statement: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers
#m and n, representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
#To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be
#merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
    #We fill the nums1 array from the end so k represents the last index of nums1.
    #i points to the last index where nums1 has elements and j does it for nums2.
        k = m + n - 1
        i, j = m - 1, n -1

        while i > -1 and j > -1:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
    
    #We fill nums1 with the remaining elements of nums2.
        while j > -1:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
        return nums1

#Testcases:
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(Solution().merge(nums1, m, nums2, n))

nums1 = [1]
m = 1
nums2 = []
n = 0
print(Solution().merge(nums1, m, nums2, n))

nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(Solution().merge(nums1, m, nums2, n))