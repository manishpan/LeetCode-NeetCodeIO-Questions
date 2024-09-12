# Problem Statement: Given an integer rowIndex, return the rowIndexth (0-indexed) row of
#  the Pascal's triangle.

class Solution:
    def getRow(self, rowIndex: int):
        res = [1]

        for i in range(rowIndex):
            next_row = [0] * (len(res) + 1)
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j+1] += res[j]
            res = next_row
        
        return res

# Testcases:
rowIndex = 3
print(Solution().getRow(rowIndex))

rowIndex = 0
print(Solution().getRow(rowIndex))

rowIndex = 1
print(Solution().getRow(rowIndex))