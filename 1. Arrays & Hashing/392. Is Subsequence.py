#Problem Statement: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
#the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
#of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s, t) -> bool:
    #For s to be subsequence of t, length of s has to be less or equal to t
        len_s = len(s)
        len_t = len(t)

    #If character matches increment i.
        i, j = 0, 0
        while i != len_s and j != len_t:
            if s[i] == t[j]:
                i += 1
            j += 1
    #If string s was completely exhausted that means s is a subsequence of t. 
        return i == len_s

#Test Cases
s = "abc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))

s = "axc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))