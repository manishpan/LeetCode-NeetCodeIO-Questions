#Problem Statement: Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

#Return the array in the form [x1,y1,x2,y2,...,xn,yn].

#Constraint:
# 1 <= nums[i] <= 10^3

class Solution:
    def shuffle(self, nums, n):
    #Since, 1 <= nums[i] <= 10^3 we are going to store xi + yi at the location i itself. For that we shift xi 10 bits
    # using the operation left shift and bitwise OR with yi.
        for i in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i + n]     #Store xi, yi at location i itself.
        
    #We create an index to store value from left. We goes from right side of array and extract x and y from the 
    # place we store it. Place y at location j, place x at location j- 1 and decrement j by 2.

        j = 2 * n - 1
        for i in range(n-1, -1, -1):
            y = nums[i] & ((1<<10) - 1)
            x = nums[i] >> 10
            nums[j] = y
            nums[j-1] = x
            j -= 2

        return nums

        


#Testcases:
nums = [2,5,1,3,4,7]
n = 3
print(Solution().shuffle(nums, n))

nums = [1,2,3,4,4,3,2,1]
n = 4
print(Solution().shuffle(nums, n))

nums = [1,1,2,2]
n = 2
print(Solution().shuffle(nums, n))