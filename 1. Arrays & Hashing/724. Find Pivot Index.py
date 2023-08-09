#Problem statement: Given an array of integers nums, calculate the pivot index of this array.

#The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum
#of all the numbers strictly to the index's right.

#If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
#This also applies to the right edge of the array.

#Return the leftmost pivot index. If no such index exists, return -1.

class Solution:
    def pivotIndex(self, nums) -> int:
    #We maintain two pointers left_sum and right_sum. Initialize it with 0 and entire sum of array.
        left_sum, right_sum = 0, sum(nums)

    #For the current element, we decrement it with right sum. If left_sum and right sum for that element are
    # equal we return it the current index. If loop exits normally, that means pivot index does not exits. So, we
    # return -1
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        
        return -1

#Testcase:
nums = [1,7,3,6,5,6]
print(Solution().pivotIndex(nums))

nums = [1,2,3]
print(Solution().pivotIndex(nums))

nums = [2,1,-1]
print(Solution().pivotIndex(nums))