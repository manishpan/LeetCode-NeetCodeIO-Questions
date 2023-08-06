#Problem statement: Given an integer numRows, return the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows: int):
    #Initializing result array with [1], since numRows > 1, 
        result = [[1]]

    #All the rows in Pascal`s triangle starts and ends with 1, so we append 1, calculate intermediate values using 
    #previous rows and then append 1 again. This row will then be added to result.
        for i in range(1, numRows):
            curr_list = [1]
            temp = result[i-1]
            for j in range(len(temp)-1):
                curr_list.append(temp[j] + temp[j+1])
            curr_list.append(1)
            result.append(curr_list)

        return result


#Test Cases
numRows = 1
print(Solution().generate(numRows))

numRows = 5
print(Solution().generate(numRows))