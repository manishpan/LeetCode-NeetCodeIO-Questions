#Problem Statement: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
#removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include
#letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
    #We initialize L and R to be beginning and ending of s.
        L, R = 0, len(s) -1

    #We increment L until we see alphanumeric character. Same for R. Then we compare L and R and changes potiners
    # accordingly
        while L < R:
            while L < R and not self.alphanumeric(s[L]):
                L += 1
            while L < R and not self.alphanumeric(s[R]):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        
        return True

#Implementing alphanumeric function    
    def alphanumeric(self, c):
        return    (ord('A') <= ord(c) <= ord('Z') or
                   ord('a') <= ord(c) <= ord('z') or
                   ord('0') <= ord(c) <= ord('9'))

#Testcases:
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))

s = "race a car"
print(Solution().isPalindrome(s))

s = " "
print(Solution().isPalindrome(s))