#Problem statement: You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

#You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

#Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

class Solution:
    def successfulPairs(self, spells, potions, success):
    #The solution is based on the approach that for spell[i] and sorted potion[j], if their product >= success, then all the subsequent potion will give result greater than success. So we first sort the potion array and then we need to find the least value in sorted potion which will give us success. We sort the array using in-built function and find the first index using binary search.
        sorted_potions = sorted(potions)
        m = len(potions)
        res = list()

        for item in spells:
            start, end = 0, m - 1

            while start <= end:
                mid = start + (end - start) // 2
                r = item * sorted_potions[mid]

                if r >= success:
                    end = mid - 1
                else:
                    start = mid + 1
                
            res.append(m - start)
        
        return res


spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(Solution().successfulPairs(spells, potions, success))

spells = [3,1,2]
potions = [8,5,8]
success = 16
print(Solution().successfulPairs(spells, potions, success))