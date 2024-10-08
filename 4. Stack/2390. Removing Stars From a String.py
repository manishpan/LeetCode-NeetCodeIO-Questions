# Problem Statement: You are given a string s, which contains stars *.

#In one operation, you can:

#Choose a star in s.
#Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Note:

# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)
        
        res = ""
        while stack:
            res = stack.pop() + res
        
        return res

# Test Cases:
s = "leet**cod*e"
print(Solution().removeStars(s))

s = "erase*****"
print(Solution().removeStars(s))