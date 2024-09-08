# Problem Statement: Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square 
# brackets is being repeated exactly k times. Note that k is guaranteed to be a positive
#  integer.

# You may assume that the input string is always valid; there are no extra white spaces, 
# square brackets are well-formed, etc. Furthermore, you may assume that the original 
# data does not contain any digits and that digits are only for those repeat numbers, k.
#  For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

class Solution:
    def decodeString(self, s: str) -> str:
    # We keep on pushing until we encount ]. When we encounter ], we form a string tmp and
    # number n and push the tmp * n.
        stack = []

        for i in range(0, len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                tmp = ''
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                
                stack.pop() # popping [

                n = ''
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                stack.append(tmp * int(n))
        
        return "".join(stack)

# Test cases:
s = "3[a]2[bc]"
print(Solution().decodeString(s))

s = "3[a2[c]]"
print(Solution().decodeString(s))

s = "2[abc]3[cd]ef"
print(Solution().decodeString(s))