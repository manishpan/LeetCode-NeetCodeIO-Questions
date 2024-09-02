# Problem Statement: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
    # We first create a hash table and we store count of each letter that is present in s in hash_table. We then again iterate over s and if the count of s[i] in hash_table is 1, we return the index, if after we have exhausted s and could not find a letter with count 1 we return -1
        hash_table = dict()

        for item in set(s):
            hash_table[item] = s.count(item)

        for i in range(len(s)):
            if hash_table[s[i]] == 1:
                return i
        
        return -1
    
# Test cases:
s = "leetcode"
print(Solution().firstUniqChar(s))

s = "loveleetcode"
print(Solution().firstUniqChar(s))

s = "aabb"
print(Solution().firstUniqChar(s))