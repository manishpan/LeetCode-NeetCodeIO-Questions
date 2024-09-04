# Problem Statement: Given an array of integers heights representing the histogram's bar 
# height where the width of each bar is 1, return the area of the largest rectangle in the
#  histogram.

class Solution:
    # We calculate the Next smaller to left and Next smaller to right of a element.
    # The NSL and NSR actually tells us the width to which a building can expand. The
    # difference of NSR - NSL tells the width and then we simply multiply it with building
    # height to get area. We then find maximum of those area
    def NSR(self, heights):
        n = len(heights)
        i = n - 1
        stack = [-1]
        res = [0] * n

        while i > -1:
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack[-1] == -1:
                res[i] = n
            else:
                res[i] = stack[-1]
            stack.append(i)
            i -= 1
        
        return res

    def NSL(self, heights):
        n = len(heights)
        i = 0
        stack = [-1]
        res = [0] * n

        while i < n:
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                stack.pop()
            res[i] = stack[-1]
            stack.append(i)
            i += 1

        return res

    def largestRectangleArea(self, heights) -> int:
        nsr, nsl = self.NSR(heights), self.NSL(heights)
        width = list()
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            width.append(nsr[i] - nsl[i] - 1)
        
        for i in range(n):
            area = heights[i] * width[i]
            max_area = max(max_area, area)
        
        return max_area

# Test cases:
heights = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(heights))

heights = [2,4]
print(Solution().largestRectangleArea(heights))