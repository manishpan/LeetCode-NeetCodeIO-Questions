#Problem Statement: Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
#For example, the array nums = [0,1,2,4,5,6,7] might become:

#[4,5,6,7,0,1,2] if it was rotated 4 times.
#[0,1,2,4,5,6,7] if it was rotated 7 times.
#Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
#[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

#Given the sorted rotated array nums of unique elements, return the minimum element of this array.

#You must write an algorithm that runs in O(log n) time.

class Solution:
    def findMin(self, nums) -> int:    
    #We initialize two pointers start and end that points to the beginning and end of nums array.
        start, end = 0, len(nums)-1

    #We can see the rotated array as two arrays, one is sorted and one is unsorted. The 
    #minimum number is always at the unsorted part. If middle number is greater than end
    # that means we are at the sorted left part of array and minimum number is at the right
    #otherwise left. We adjust the start and end pointers accordingly.
        while start < end:
            mid = start + ((end - start) >> 1)

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        
        return nums[start]

#Testcases:
nums = [3,4,5,1,2]
print(Solution().findMin(nums))

nums = [4,5,6,7,0,1,2]
print(Solution().findMin(nums))

nums = [11,13,15,17]
print(Solution().findMin(nums))