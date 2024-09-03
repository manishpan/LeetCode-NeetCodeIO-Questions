# Problem statement: Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures):
    # Since we have to look right to find the next greater element than the current one, we initialize i to come from right. We also initialize stack = [-1] and res array.
        n = len(temperatures)
        i = n - 1
        stack = [-1]
        res = [0] * n

    # We iterate through the array from right, if stack is empty(i.e it has -1 on top) 
    # that means there is no day hotter than the current day hence we put 0 in res array
    # if stack top does indicate a day, then we subtract that day index with i to get
    # the count of number of days that has passed. 
        while i > -1:
            while stack[-1] != -1 and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack[-1] == -1:
                res[i] = 0
            else:
                res[i] = stack[-1] - i
            stack.append(i)
            i -= 1
        
        return res

# Test cases:
temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))

temperatures = [30,40,50,60]
print(Solution().dailyTemperatures(temperatures))

temperatures = [30,60,90]
print(Solution().dailyTemperatures(temperatures))