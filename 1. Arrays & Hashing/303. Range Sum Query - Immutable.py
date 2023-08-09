#Problem statement: Given an integer array nums, handle multiple queries of the following type:

#Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
#Implement the NumArray class:

#NumArray(int[] nums) Initializes the object with the integer array nums.
#int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
#(i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:
#We will maintain a prefix sum array that will hold the sum from 0 to till index i.
    def __init__(self, nums):
        self.prefix_sums = []
        sum = 0

        for i in nums:
            sum += i
            self.prefix_sums.append(sum)
#Since, we have prefix_sum, the answer would simple by difference between prefix_sums[right] - prefix_sums[left-1].
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sums[right]
        return self.prefix_sums[right] - self.prefix_sums[left-1]

#Testcases:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))