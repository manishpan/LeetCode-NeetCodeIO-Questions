#Problem Statement: Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
#The guards have gone and will come back in h hours.

#Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats
#k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any
#more bananas during this hour.

#Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

#Return the minimum integer k such that she can eat all the bananas within h hours.

import math

class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
    #We define start and end to be the search space where k can be. We apply binary search to calculate the potential
    #value of k and calculate hours_taken to eat all the piles. If hourse_taken > h, that means we were too slow
    # so we move start pointer otherwise we store result and move end pointer.
        start, end = 1, max(piles)
        k = end

        while start <= end:
            hours_taken = 0
            mid = start + ((end - start) // 2)

            for i in piles:
                hours_taken += math.ceil(i/mid)
            
            if hours_taken <= h:
                end = mid - 1
                k = min(mid, k)
            else:
                start = mid + 1
            
        return k
    
#Testcases:
piles = [3,6,7,11]
h = 8
print(Solution().minEatingSpeed(piles, h))

piles = [30,11,23,4,20]
h = 5
print(Solution().minEatingSpeed(piles, h))

piles = [30,11,23,4,20]
h = 6
print(Solution().minEatingSpeed(piles, h))

piles = [312884470]
h = 312884469
print(Solution().minEatingSpeed(piles, h))

piles = [312884470]
h = 968709470
print(Solution().minEatingSpeed(piles, h))