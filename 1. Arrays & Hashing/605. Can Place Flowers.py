#Problem Statement: You have a long flowerbed in which some of the plots are planted, and some are not. However,
#flowers cannot be planted in adjacent plots.

#Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
#return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false
#otherwise.

class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
    #Adding 0 to start and end of flowerbed so that we can calculate sum in a window of 3
        new_flowerbed = [0] + flowerbed + [0]
    
    #Calculating sum in window of 3. If sum is 0 then thats means we can plant a flower and hence we decrement n by 1.
    #If n becomes 0 or negative we return True as we have exhausted all the flowers that could be planted.
        for i in range(1, len(new_flowerbed) - 1):
            sum3 = new_flowerbed[i-1] + new_flowerbed[i] + new_flowerbed[i+1]
            if sum3 == 0:
                new_flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
            
        return False
        
#Testcases:
flowerbed = [1,0,0,0,1]
n = 1
print(Solution().canPlaceFlowers(flowerbed, n))

flowerbed = [1,0,0,0,1]
n = 2
print(Solution().canPlaceFlowers(flowerbed, n))