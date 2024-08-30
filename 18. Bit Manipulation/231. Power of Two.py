# Problem Statement:Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2**x.

class Solution:
    def isPowerofTwo(self, n):
    # If n is a power of 2, then it should have only 1 bit high and should be of the form 10000..... if we subtract 1 from n then we will get n of the form 0111... . We then perform bitwise & between n and n-1, if we get 0 then n is a power of 2.
        if n == 0:
            return False
        if n & (n - 1) == 0:
            return True
        return False

n = 1
print(Solution().isPowerofTwo(n))

n = 16
print(Solution().isPowerofTwo(n))

n = 3
print(Solution().isPowerofTwo(n))

n = 0
print(Solution().isPowerofTwo(n))