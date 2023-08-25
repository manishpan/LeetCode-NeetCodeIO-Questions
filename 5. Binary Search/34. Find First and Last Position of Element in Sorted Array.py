#Problem Statement: Given an array of integers nums sorted in non-decreasing order, find the starting and ending
#position of a given target value.

#If target is not found in the array, return [-1, -1].

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums, target: int):
    # We write two auxillary function Occurence with leftBias added to it. When leftBias is True, the occurence fxn
    # returns the leftmost occurence of target and when False it returns the rightmost occurence of target.
        def Occurence(nums, target, leftBias):
            L, R = 0, len(nums) - 1
            i = -1

            while L <= R:
                mid = L + ((R - L) // 2)

                if nums[mid] > target:
                    R = mid - 1
                elif nums[mid] < target:
                    L = mid + 1
                else:
                    i = mid
                    if leftBias:
                        R = mid - 1
                    else:
                        L = mid + 1
            
            return i

        fo = Occurence(nums, target, True)

        if fo == -1:
            return [-1, -1]
        return [fo, Occurence(nums, target, False)]

#Testcases:
nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums, target))

nums = [5,7,7,8,8,10]
target = 6
print(Solution().searchRange(nums, target))

nums = []
target = 0
print(Solution().searchRange(nums, target))

nums = [1]
target = 1
print(Solution().searchRange(nums, target))