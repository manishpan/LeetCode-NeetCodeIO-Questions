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
    #If the first element is smaller than the last element, then the array is sorted and minimum element is at 0.
        if nums[0] <= nums[-1]:
            return nums[0]
    
    #We initialize two pointers L and R that points to the beginning and end of nums array.
        L, R = 0, len(nums)-1

    #An element is minimum element if the element that is to left of it is greater. We calculate mid and check if it
    # is greater than mid - 1. If it is we return mid element otherwise we will need to go to the part where array
    # is not sorter. For that, we compare mid element to first or last element and changes L or R accordingly.
        while L <= R:
            mid = L + ((R - L) // 2)

            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[-1]:
                L = mid + 1
            elif nums[mid] < nums[0]:
                R = mid - 1

#Testcases:
nums = [3,4,5,1,2]
print(Solution().findMin(nums))

nums = [4,5,6,7,0,1,2]
print(Solution().findMin(nums))

nums = [11,13,15,17]
print(Solution().findMin(nums))