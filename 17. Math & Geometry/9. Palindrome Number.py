#Problem Statement: Given an integer x, return true if x is a palindrome and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
    #One approach is to reverse the number using rN = rN * 10 + x % 10 and compare it with number. Another approach
    #is to compare leftmost and rightmost value of the number. If it matches, we remove both right and left digits,
    #But first, if number is negative we return False immediately, if number is single digit we return True.

        if x < 0:   return False
        if x % 10 == x: return True

    # Calculating divisor
        div = 1
        while x >= 10 * div:
            div *= 10
    #We remove left and right digits and compare it. If it matches, we remove rightmost digit(using x % div) and then
    # leftmost digit using x // 10    
        while x > 0:
            LeftN = x % 10
            RightN = x // div

            if LeftN != RightN:
                return False
            
            x = x % div
            x = x // 10
            div //= 100
        
        return True

#Testcases:
x = 121
print(Solution().isPalindrome(x))

x = -121
print(Solution().isPalindrome(x))

x = 10
print(Solution().isPalindrome(x))