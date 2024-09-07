# Problem statment: Design an algorithm that collects daily price quotes for some stock
#  and returns the span of that stock's price for the current day.

#The span of the stock's price in one day is the maximum number of consecutive days 
# (starting from that day and going backward) for which the stock price was less than 
# or equal to the price of that day.

#For example, if the prices of the stock in the last four days is [7,2,1,2] and the price
#  of the stock today is 2, then the span of today is 4 because starting from today, the
#  price of the stock was less than or equal 2 for 4 consecutive days.
#Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of 
# the stock today is 8, then the span of today is 3 because starting from today, the 
# price of the stock was less than or equal 8 for 3 consecutive days.
#Implement the StockSpanner class:

#StockSpanner() Initializes the object of the class.
#int next(int price) Returns the span of the stock's price given that today's price is
#  price.

class StockSpanner:
    # if stack top > price, we store that index in stack. Otherwise we keep on popping 
    # unless we encounter a price >= stack top. In that case we store index - stack[top]
    # and that gives us the stock span.
    def __init__(self):
        self.prices = list()
        self.stack = [-1]
        self.res = list()
        self.i = 0

    def next(self, price: int) -> int:
        self.prices.append(price)

        while self.stack[-1] != -1 and self.prices[self.stack[-1]] <= self.prices[self.i]:
            self.stack.pop()
        self.res.append(self.i - self.stack[-1])
        self.stack.append(self.i)
        self.i += 1

        return self.res[-1]

# Test cases:
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
calls = [[], [100], [80], [60], [70], [60], [75], [85]]

for i in calls:
    if not i:
        obj = StockSpanner()
    else:
        print(obj.next(price=i[0]))
