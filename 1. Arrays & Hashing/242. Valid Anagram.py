#Problem Statement: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    count = [0] * 256
    for i in s:
        count[ord(i)] += 1
    for j in t:
        count[ord(j)] -= 1
    
    if 1 in count:
        return False
    return True


s = 'slient'
t = 'listey'

print(isAnagram(s,t))