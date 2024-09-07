# Problem Statement: We are given an array asteroids of integers representing asteroids 
# in a row.

#For each asteroid, the absolute value represents its size, and the sign represents its 
# direction (positive meaning right, negative meaning left). Each asteroid moves at the 
# same speed.

#Find out the state of the asteroids after all collisions. If two asteroids meet, 
# the smaller one will explode. If both are the same size, both will explode. 
# Two asteroids moving in the same direction will never meet.

class Solution:
    def asteroidCollision(self, asteroids):
    # A collision will occur only when stack top is a +ve element and asteroid is -ve.
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                collision = a + stack[-1]
                
                if collision > 0:
                    a = 0
                elif collision < 0:
                    stack.pop()
                else:
                    a = 0
                    stack.pop()
            
            if a:
                stack.append(a)
        
        return stack


# Test cases:
asteroids = [5,10,-5]
print(Solution().asteroidCollision(asteroids))

asteroids = [8,-8]
print(Solution().asteroidCollision(asteroids))

asteroids = [10,2,-5]
print(Solution().asteroidCollision(asteroids))