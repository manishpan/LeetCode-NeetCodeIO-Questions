#problem statement: Given an array of integers nums and an integer target, return indices of the two numbers such
#that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

#The following solution is O(n2)
def twoSum(nums, target):
    indices = []
    i , j = 0, 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                indices.append(i)
                indices.append(j)
                return indices
            
def twoSum2(nums, target):
    hashMap = dict()
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[nums[i]] = i
            
nums = [2,1,5,3]
target = 4
print(twoSum2(nums, target))