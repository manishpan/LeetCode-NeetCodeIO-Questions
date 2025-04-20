# # Problem statement: You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])

        start, end = 0, m-1
        while start <= end:
            row = (start + end) >> 1

            if matrix[row][0] == target or target == matrix[row][m-1]:
                return True
            if matrix[row][0] < target < matrix[row][m-1]:
                break
            elif matrix[row][0] > target:
                end = row - 1
            else:
                start = row + 1
        
        if start > end:
            return False
        
        start, end = 0, n-1
        while start <= end:
            mid = (start + end) >> 1
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return False

# Test cases:
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Solution().searchMatrix(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(Solution().searchMatrix(matrix, target))