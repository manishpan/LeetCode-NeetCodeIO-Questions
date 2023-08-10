#Problem statement: Given a pattern and a string s, find if s follows the same pattern.

#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
    #Creating a list of words from string s. We could also have used s.split(' ').
        i, word = 0, ""
        words = []
        len_s = len(s)
        while i <= len_s:
            if i == len_s or s[i] == " ":
                words.append(word)
                word = ""
            else:
                word += s[i]
            i += 1

    #In order to have a bijection between pattern and s, the length of pattern and numbers of words in s have to be
    #  equal.
        if len(pattern) != len(words):
            return False

    #Creating two hashMaps to store s to pattern mapping and p to s mapping.    
        mappingSP, mappingPS = {}, {}

    #If p in mappingPS and it`s already mapped to some other value, we return False. Same for mappingSP.`
        for p, w in zip(pattern, words):
            if (p in mappingPS and mappingPS[p] != w) or (w in mappingSP and mappingSP[w] != p):
                return False
            else:
                mappingPS[p] = w
                mappingSP[w] = p
    
    #If loops exits normally that means there is no mismatch, hence we return True    
        return True
        
#Testcases:
pattern = "abba"
s = "dog cat cat dog"
print(Solution().wordPattern(pattern, s))

pattern = "abba"
s = "dog cat cat fish"
print(Solution().wordPattern(pattern, s))

pattern = "aaaa"
s = "dog cat cat dog"
print(Solution().wordPattern(pattern, s))