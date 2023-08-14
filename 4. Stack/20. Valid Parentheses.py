#Problem statement: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
#the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
    #For s to be valid, its length must be even. If it is odd we return False
        if len(s) & 1:  return False
    
    #We create mapping of closing parenthesis to open parenthesis and a stack to store open parenthesis.
        stack = []
        parenthesis = {')':'(', '}':'{', ']':'['}

    #Iterating through s, if i is opening parenthesis we push it into the stack. If s is closing parenthesis, we
    # match the type of top of stack and i, if they are different we return False
        for i in s:
            if i in parenthesis:
                if stack and stack[-1] == parenthesis[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if stack:   return False
        return True

#Testcases:
s = "()"
print(Solution().isValid(s))

s = "()[]{}"
print(Solution().isValid(s))

s = "(]"
print(Solution().isValid(s))