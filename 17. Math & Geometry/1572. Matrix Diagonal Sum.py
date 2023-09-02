#Problem Statement: Given a square matrix mat, return the sum of the matrix diagonals.

#Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that
#are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat) -> int:
    #We first calculate dimension of msquare matrix and initialize variables res that stores the sum of primary and
    # secondary diagonal
        n = len(mat)
        res = 0

        for i in range(n):
            res += mat[i][i]     #Primary diagonal
            res += mat[i][n-i-1] #Secondary diagonal
        
    #If n is odd, then we have considered middle element of stack two times. We need to separete it from the sum.
        mid = mat[n//2][n//2] if n & 1 else 0

        return res - mid


#Testcases:
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(Solution().diagonalSum(mat))

mat = [[1,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]]
print(Solution().diagonalSum(mat))