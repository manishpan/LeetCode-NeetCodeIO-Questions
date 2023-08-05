#Problem statement: Given an integer array nums of length n, you want to create an array ans of length 2n where 
#ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

#Specifically, ans is the concatenation of two nums arrays.

#Return the array ans.

def getConcatenation(nums, val):
    n = len(nums)
    ans = [0] * val * n
    for c in range(val):
        for i in range(n):
            ans[i + n * c] = nums[i]
    return ans

nums = [1,2,2]
print(getConcatenation(nums,3))