#Problem Statement: Given a sorted array of distinct integers and a target value, return the index if the target is
#found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums, target: int) -> int:
    #We create two pointers low and high that represents beginning and ending of nums array.    
        low, high = 0, len(nums) - 1

    #Calculate mid, and changes low and high accordingly. In that sense, we have eliminated half of checking.
    #If target is found we return mid index.
    #If nums is very very large, languages such as C++ and Java may throw an integer overflow error. So, in that
    #case a better way would be to calculate distance between high and low, divide it by 2 and add it to low to
    #get middle element.
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
    
    #If the loop exits normally, that means we did not find target in nums array. In that case we have to return
    #its possible index. low will represents where the target should be placed.
        return low

#Testcases:
nums = [1,3,5,6]
target = 5
print(Solution().searchInsert(nums, target))

nums = [1,3,5,6]
target = 2
print(Solution().searchInsert(nums, target))

nums = [1,3,5,6]
target = 7
print(Solution().searchInsert(nums, target))