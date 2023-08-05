#Problem Statement: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
#the original letters exactly once.

class Solution:
    def isAnagram(self, s, t) -> bool:
    #Anagrams must have same length. If they differ in length they cannot be anagram
        if len(s) != len(t):
            return False
    
    #Count array of length 256 to mark if we have seen an character or not
        count = [0] * 256

    #If a character is in s, +1 is marked as flag and in t that flag is once again down.
        for i in range(len(s)):
            count[ord(s[i])] += 1
            count[ord(t[i])] -= 1
    
    #If all the flags are down, then that means they are anagrams
        for x in count:
            if x != 0:
                return False
        return True

#Sample Test Cases
s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))

s = "rat"
t = "car"
print(Solution().isAnagram(s, t))