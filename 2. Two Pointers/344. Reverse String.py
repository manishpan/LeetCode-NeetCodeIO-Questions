#Problem statement: Write a function that reverses a string. The input string is given as an array of characters s.

#You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s) -> None:
    #We create two pointers L and R pointing to beginning and ending and swap the values until L < R.
    #Other solutions involve using stack and it can be done using recursion as well.
        L, R = 0, len(s) - 1

        while L < R:
            s[L], s[R] = s[R], s[L]
            L, R = L + 1, R - 1
        
        return s

#Testcases:
s = ["h","e","l","l","o"]
print(Solution().reverseString(s))

s = ["H","a","n","n","a","h"]
print(Solution().reverseString(s))