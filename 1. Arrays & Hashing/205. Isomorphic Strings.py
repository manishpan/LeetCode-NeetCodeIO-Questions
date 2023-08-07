#Problem statement: Given two strings s and t, determine if they are isomorphic.

#Two strings s and t are isomorphic if the characters in s can be replaced to get t.

#All occurrences of a character must be replaced with another character while preserving the order of characters.
#No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
    #Creating two hashMaps that stores mapping from s to t and t to s.
        mapST, mapTS = {}, {}

    #If a character has already been mapped and it is being mapped to another character then we return False.
        for i in range(len(s)):
            s1, t1 = s[i], t[i]
            if ((s1 in mapST and mapST[s1] != t1) or 
                (t1 in mapTS and mapTS[t1] != s1)):
                return False
            mapST[s1] = t1
            mapTS[t1] = s1

    #If we exited the loop completely that means s and t are isomorphic hence return True            
        return True

#TestCases:
s = "egg"
t = "add"
print(Solution().isIsomorphic(s, t))

s = "foo"
t = "bar"
print(Solution().isIsomorphic(s, t))

s = "paper"
t = "title"
print(Solution().isIsomorphic(s, t))