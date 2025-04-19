# # Problem Statement: A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

class Solution(object):
    def shipWithinDays(self, weights, days):
        # This problem is similar to split array largest sum problem. We initilize start, end. This gives us possible range of capacity we can carry. After that we check each capacity if its optimal for  the days given or not.
        def canCarry(mid):
            days_needed = 1
            sum = 0

            for i in range(len(weights)):
                sum += weights[i]
                if sum > mid:
                    days_needed += 1
                    sum = weights[i]
                if days_needed > days:
                    return False
            return True
        
        start, end = max(weights), sum(weights)
        res = -1

        while start <= end:
            mid = start + ((end - start) >> 1)

            if canCarry(mid):
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return res

# Testcases:
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(Solution().shipWithinDays(weights, days))

weights = [3,2,2,4,1,4]
days = 3
print(Solution().shipWithinDays(weights, days))

weights = [1,2,3,1,1]
days = 4
print(Solution().shipWithinDays(weights, days))