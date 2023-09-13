#Problem Statement: Given an integer columnNumber, return its corresponding column title as it appears in an
#Excel sheet.

class Solution:
#The letter for excel column title can be found by subtracting minus 1 and taking modulus 26. After that we will
#divide the columnNumber by 26.
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            res = chr(ord('A') + offset) + res
            columnNumber = (columnNumber - 1) // 26
        
        return res

#Testcases:
columnNumber = 1
print(Solution().convertToTitle(columnNumber))

columnNumber = 28
print(Solution().convertToTitle(columnNumber))

columnNumber = 701
print(Solution().convertToTitle(columnNumber))