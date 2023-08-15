#Problem Statement: You have n coins and you want to build a staircase with these coins. The staircase consists of k
#rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

#Given the integer n, return the number of complete rows of the staircase you will build.

class Solution:
    def arrangeCoins(self, n: int) -> int:
    #Suppose k rows have been filled entirely. In that case, 1+2+3+...+k <= n. The left side of inequality is the
    #sum of first k natural numbers which is equal to k(k+1)/2. So, inequality becomes, k(k+1)/2 <= n.
    #Solving for k we get the quadratic equation, k^2+k-2n <= n. 
    #We take the positive root of the equation which is (-1+D)/2 where D is discriminat and is equal to 
    # sqrt(-1 + 8 * n)

        D = pow(-1+8*n, 0.5)

        k = (-1+D) // 2
        return int(k) 
    
    #Binary Search Solution

    #We initialize two pointers l, r to be 1 and n respectively.
        l, r = 1, n
        res = 0

        while l <= r:
            mid = (l + r) // 2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                r = mid - 1
            else:
                l = mid - 1
                res = max(res, mid)
        
        return res


#Testcases:
n = 5
print(Solution().arrangeCoins(n))

n = 8
print(Solution().arrangeCoins(n))