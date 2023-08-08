#Problem Statement: Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
#always exists in the array.

class Solution:
    def majorityElement(self, nums) -> int:
    #Variables count and curr holds the count of curr element.
        count, curr = 0, 0

    #If curr_element differs from i we decrement count otherwise increment it. If count becomes 0 and next element
    #  differs we set curr to new element and makes it count 1.
    #The majority element will have the count > 1 since the frequency of majority element is n / 2.
        for i in nums:
            if count == 0:
                curr = i
                count = 1
            else:
                if curr == i:
                    count += 1
                else:
                    count -= 1
        
        return curr

#TestCases:
nums = [6,5,5]
print(Solution().majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))