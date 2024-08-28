#Problem Statement: Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
#The returned integer should be non-negative as well.

#You must not use any built-in exponent function or operator.

#For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution:
    def mySqrt(self, x: int) -> int:
    #We first points L, R to be 1 and x. We calculate the middle of the number series and sqr it. The squared
    # value can be less, greater than or equal to x, so we changes R, L or return mid accordingly. If the loop exits
    # normally, that means sqrt of x is not an integer. In that case, L-1 will point to round down integer of sqrt of
    # x.
        L, R = 1, x

        while L <= R:
            mid = L + (R - L) // 2
            sqr = mid * mid

            if sqr > x:
                R = mid - 1
            elif sqr < x:
                L = mid + 1
            else:
                return mid
        
        return R


#Testcases:
x = 4
print(Solution().mySqrt(x))

x = 8
print(Solution().mySqrt(x))

x = 0
print(Solution().mySqrt(x))

x = 1
print(Solution().mySqrt(x))