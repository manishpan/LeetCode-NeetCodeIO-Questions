# Problem Statement: Given two integer arrays pushed and popped each with distinct values,
#  return true if this could have been the result of a sequence of push and pop operations
#  on an initially empty stack, or false otherwise.

class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
    # We initialize push and pop pointer. We keep on pushing onto stack untill stack top 
    # is not equal to popped[pop]. When it equals we keep on popping untill it is not equal
    # to popped[pop]. Finally, if at last stack is not empty that means we could not find
    # a valid sequence so we return False, otherwise True
        push, pop = 0, 0
        stack = [-1]

        while push < len(pushed):
            stack.append(pushed[push])
            push += 1
            while stack[-1] != -1 and stack[-1] == popped[pop]:
                stack.pop()
                pop += 1
        
        if stack[-1] != -1:
            return False
        return True

# Test cases:
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(Solution().validateStackSequences(pushed, popped))

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(Solution().validateStackSequences(pushed, popped))