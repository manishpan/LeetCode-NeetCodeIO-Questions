#Problem statement: You are keeping the scores for a baseball game with strange rules. At the beginning of the game,
#you start with an empty record.

#You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record
#and is one of the following:

#An integer x.
#Record a new score of x.
#'+'.
#Record a new score that is the sum of the previous two scores.
#'D'.
#Record a new score that is the double of the previous score.
#'C'.
#Invalidate the previous score, removing it from the record.
#Return the sum of all the scores on the record after applying all the operations.

class Solution:
    def calPoints(self, operations) -> int:
    #We store scroes in scores stack.   
        scores = []
    #We do the operations as given in the operations list. And at last we return the sum of scores.
        for i in operations:
            if i == '+':
                scores.append(scores[-1] + scores[-2])
            elif i == 'D':
                scores.append(2 * scores[-1])
            elif i == 'C':
                scores.pop()
            else:
                scores.append(int(i))
        
        return sum(scores)

#Testcases:
ops = ["5","2","C","D","+"]
print(Solution().calPoints(ops))

ops = ["5","-2","4","C","D","9","+","+"]
print(Solution().calPoints(ops))

ops = ["1","C"]
print(Solution().calPoints(ops))