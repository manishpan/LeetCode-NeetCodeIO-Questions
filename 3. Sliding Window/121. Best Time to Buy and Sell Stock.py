#Problem Statement: You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
#future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices) -> int:
    #We initialize maxPrice, maxProfit to 0. We traverse from right side of array and calculate profit. We update 
    # maxProfit is current profit is greater than previous maxProfit. We also update to see if current price is 
    # greater than maxPrice or not. 
        maxPrice = 0
        maxProfit = 0
        i = len(prices) - 1

        while i > -1:
            profit = maxPrice - prices[i]
            maxProfit = max(maxProfit, profit)
            maxPrice = max(maxPrice, prices[i])
            i -= 1
        
        return maxProfit

#Testcases:
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))

prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))