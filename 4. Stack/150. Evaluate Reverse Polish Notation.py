#Problem Statement: You are given an array of strings tokens that represents an arithmetic expression in a
#Reverse Polish Notation.

#Evaluate the expression. Return an integer that represents the value of the expression.

#Note that:

#The valid operators are '+', '-', '*', and '/'.
#Each operand may be an integer or another expression.
#The division between two integers always truncates toward zero.
#There will not be any division by zero.
#The input represents a valid arithmetic expression in a reverse polish notation.
#The answer and all the intermediate calculations can be represented in a 32-bit integer.

class Solution:
    def evalRPN(self, tokens) -> int:
    #We create a stack, if we see operand we push it onto stack. If we see operator, we pop two above elements
    #from stack(operand 2 comes first and then operand 1) and perform operation. We push the result back onto stack.
        stack = []

        for i in tokens:
            if i not in {'+', '-', '*', '/'}:
                stack.append(int(i))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '+':
                    stack.append(op1 + op2)
                elif i == '-':
                    stack.append(op1 - op2)
                elif i == '*':
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 / op2))
        return stack.pop()
        

#Testcases:
tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))

tokens = ["4","13","5","/","+"]
print(Solution().evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))

tokens = ["4","-2","/","2","-3","-","-"]
print(Solution().evalRPN(tokens))