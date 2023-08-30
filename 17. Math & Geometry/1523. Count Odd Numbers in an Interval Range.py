#Problem Statement: Given two non-negative integers low and high. Return the count of odd numbers between low and
#high (inclusive).

class Solution:
    def countOdds(self, low: int, high: int) -> int:
    #First we calculate number of integers that lie between low and high(inclusive).
        rang = high - low + 1
    #Next we calculate number of odd values that lie between low and high(inclusive). We have to add 1
    #when both low and high are odd numbers.
        odd_numbers = rang // 2 + (low & 1 and high & 1)
        return odd_numbers

#Testcases:
low = 3
high = 7
print(Solution().countOdds(low, high))

low = 8
high = 10
print(Solution().countOdds(low, high))