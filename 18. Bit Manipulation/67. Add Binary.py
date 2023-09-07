#Problem statement: Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        diff = len(a) - len(b)
        carry = False
        res = ""
        stack = []

    #We are maing a and b of equal length by adding 0 to the front of whatever is shorter.
        if diff > 0:
            while diff:
                b = "0" + b
                diff -= 1
        else:
            while diff:
                a = "0" + a
                diff += 1
        
        i = len(a) - 1

    #Traversing through entire numbers and adding result to the stack and adding carry as needed.
        while i > -1:
            if a[i] == b[i]:
                if carry:
                    stack.append("1")
                else:
                    stack.append("0")
    
                carry = True if a[i] == "1" else False
            else:
                if carry:
                    stack.append("0")
                    carry = True
                else:
                    stack.append("1")

            i -= 1

        if carry:
            res = "1" + res
        
        while stack:
            res = res + stack.pop()

        return res  

#Testcases:
a = "11"
b = "1"
print(Solution().addBinary(a, b))

a = "1010"
b = "1011"
print(Solution().addBinary(a, b))