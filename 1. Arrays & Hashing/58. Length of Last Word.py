#Problem statement: Given a string s consisting of words and spaces, return the length of the last word in the string.

#A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    #length variable will be the length og the last word and i will point to first character when traversed from right    
        i, length = len(s) - 1, 0

    #Finding the index of first character from right side skipping space.
        while s[i] == ' ':
            i -= 1

    #Calculating length of last word until we see space
        while i > -1 and s[i] != ' ':
            length += 1
            i -= 1

        return length

#Test Cases

s = "Single"
print(Solution().lengthOfLastWord(s))

s = "Hello World"
print(Solution().lengthOfLastWord(s))

s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))

s = "luffy is still joyboy"
print(Solution().lengthOfLastWord(s))