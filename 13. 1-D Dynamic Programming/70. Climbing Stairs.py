#Problem Statement: You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        f1, f2 = 1, 2

        while n > 2:
            res = f1 + f2
            f1, f2 = f2, res
            n -= 1
        
        return f2

#Testcase:
n = 2
print(Solution().climbStairs(n))

n = 3
print(Solution().climbStairs(n))