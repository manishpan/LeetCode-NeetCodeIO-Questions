#Problem statement: Given a string s, return true if the s can be palindrome after deleting at most one character
#from it.

class Solution:
    def validPalindrome(self, s: str) -> bool:
    #We initialize L and R pointers to the beginning and ending of s.
        L, R = 0, len(s) - 1

    #Checking if characters at L and R matches or not. If it doesn`t and since we can skip one character, we check both
    # the possibility of from [L+1, R] and [L, R-1]. If both of them are not palindrome we return False otherwise True.`
        while L < R:
            if s[L] != s[R]:
                return self.isPalindrome(s, L+1, R) or self.isPalindrome(s, L, R-1)
            L, R = L + 1, R - 1
        
        return True
    
    #We create a helper function that takes indices and tells if string s is palindrome or not.
    def isPalindrome(self, s, L, R):
        while L < R:
            if s[L] != s[R]:
                return False
            L, R = L + 1, R - 1
        return True

#Testcases:
s = "aba"
print(Solution().validPalindrome(s))

s = "abca"
print(Solution().validPalindrome(s))

s = "abc"
print(Solution().validPalindrome(s))

s = "bcbc"
print(Solution().validPalindrome(s))