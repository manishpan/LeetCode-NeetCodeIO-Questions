#Problem statement: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such
#that each unique element appears only once. The relative order of the elements should be kept the same. Then return
#the number of unique elements in nums.

#Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

#Change the array nums such that the first k elements of nums contain the unique elements in the order they were 
#present in nums initially. The remaining elements of nums are not important as well as the size of nums.
#Return k.

class Solution:
    def removeDuplicates(self, nums) -> int:
    #ind points to the element where we will place next unique value. The element at index 0 will remain at 0.    
        ind = 1

    #If the previous and next element are not same that`s means we are seeing a unique value and hence place that
    # value at ind and increment ind.`
        for i in range(1, len(nums)): 
            if nums[i] != nums[i-1]:
                nums[ind] = nums[i]
                ind += 1

        return nums[:ind]

#Testcases:
nums = [1,1,2]
print(Solution().removeDuplicates(nums))

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))

nums = [1,2,2]
print(Solution().removeDuplicates(nums))