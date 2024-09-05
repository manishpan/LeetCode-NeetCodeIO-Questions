# Problem Statement: Given a string s of lower and upper case English letters.

#A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

#0 <= i <= s.length - 2
#s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
#To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

#Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

#Notice that an empty string is also good.

class Solution:
    def makeGood(self, s: str) -> str:
    # We make a stack and keep on storing elements onto the stack. We then match it with
    #  current element we are seeing. If the ASCII value difference is 32 then they are
    #  uppercase lowercase pair and we pop it from stack.
        n = len(s)
        i = 0
        stack = []
        diff = ord('a') - ord('A')

        while i < n:
            while stack and abs(ord(stack[-1]) - ord(s[i])) == diff:
                stack.pop()
                i += 1
            if i < n:
                stack.append(s[i])
            i += 1
        
        res = ""
        while stack:
            res = stack.pop() + res
        
        return res


# Test cases:
s = "leEeetcode"
print(Solution().makeGood(s))

s = "abBAcC"
print(Solution().makeGood(s))

s = "s"
print(Solution().makeGood(s))