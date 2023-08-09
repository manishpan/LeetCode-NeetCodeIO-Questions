#Problem Statement: The next greater element of some element x in an array is the first greater element that is to 
#the right of x in the same array.

#You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

#For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater
#element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

#Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

class Solution:
    def nextGreaterElement(self, nums1, nums2):
    #Initializing lengths of nums1 and nums2, stack to hold values that are in nums1 and result to store result.
        l1, l2 = len(nums1), len(nums2)
        stack = []
        result = [-1] * l1

    #Creating a mapping value:index. This will help us to search if an element exists in nums1 or not.
        nums1_map = {nums1[i]:i for i in range(l1)}

    #For every element in  nums2, check if top of stack is less than current value, pop the top, retrieve its index
    #from nums1_map and store current in result.
    #If current exists in nums1 only then add the cur to stack.
        for i in range(l2):
            cur = nums2[i]
            while stack and stack[-1] < cur:
                temp = stack.pop()
                ind = nums1_map[temp]
                result[ind] = cur
            if cur in nums1_map:
                stack.append(cur)
        
        return result        

#Testcases:
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(Solution().nextGreaterElement(nums1, nums2))

#nums1 = [2,4]
#nums2 = [1,2,3,4]
#print(Solution().nextGreaterElement(nums1, nums2))