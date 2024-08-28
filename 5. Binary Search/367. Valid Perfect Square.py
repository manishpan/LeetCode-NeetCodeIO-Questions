#Problem statement: Given a positive integer num, return true if num is a perfect square or false otherwise.

#A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer
#with itself.

#You must not use any built-in library function, such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
    #We initialize L and R to be 1 and num itself. This will be helpful in calculating the middle value and check
    # if the square of middle value if lesser, greater or equal to num. We changes L, R or return True accordingly.    
        L, R = 1, num

        while L <= R:
            mid = (L + R) // 2
            sqr = mid ** 2

            if sqr > num:
                R = mid - 1
            elif sqr < num:
                L = mid + 1
            else:
                return True
        
        return False

#Testcases:
num = 16
print(Solution().isPerfectSquare(num))

num = 14
print(Solution().isPerfectSquare(num))

num = 1
print(Solution().isPerfectSquare(num))