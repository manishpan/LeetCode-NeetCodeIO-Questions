#Problem statement: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#Implement the MinStack class:

#MinStack() initializes the stack object.
#void push(int val) pushes the element val onto the stack.
#void pop() removes the element on the top of the stack.
#int top() gets the top element of the stack.
#int getMin() retrieves the minimum element in the stack.
#You must implement a solution with O(1) time complexity for each function.

# Implementation using extra stack
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.minStack = []
        
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if not self.minStack or self.minStack[-1] >= val:
#             self.minStack.append(val)

#     def pop(self) -> None:
#         if self.stack[-1] == self.minStack[-1]:
#             self.minStack.pop()
#         self.stack.pop()
        
#     def top(self) -> int:
#         return self.stack[-1] 

#     def getMin(self) -> int:
#         return self.minStack[-1]
    
# Implementation without using any secondary stack

class MinStack:
    def __init__(self):
        self.stack = []
        self.ME = -1

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.ME = val
        else:
            if self.ME < val:
                self.stack.append(val)
            elif self.ME >= val:
                self.stack.append(2 * val - self.ME)
                self.ME = val            

    def pop(self) -> None:
        if not self.stack:
            return -1
        if self.stack[-1] > self.ME:
            self.stack.pop()
        elif self.stack[-1] <= self.ME:
            self.ME = 2 * self.ME - self.stack[-1]
            self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return -1
        if self.stack[-1] > self.ME:
            return self.stack[-1]
        elif self.stack[-1] <= self.ME:
            return self.ME

    def getMin(self) -> int:
        if not self.stack:
            return -1
        return self.ME

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#Testcase:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())