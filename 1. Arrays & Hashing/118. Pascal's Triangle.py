#Problem statement: Given an integer numRows, return the first numRows of Pascal's triangle.

def generate(numRows):
    op = [[1]]
    for i in range(1, numRows):
        temp = []
        temp.append(1)
        for j in range(i-1):
            temp.append(op[i-1][j] + op[i-1][j+1])
        temp.append(1)
        op.append(temp)
    return op

numRows = 10
print(generate(numRows))