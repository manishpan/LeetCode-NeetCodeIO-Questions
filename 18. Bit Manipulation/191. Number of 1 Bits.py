#Problem Statement: Write a function that takes the binary representation of an unsigned integer and returns the
#number of '1' bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
    #Since every n is always going to be 32 bit, the while loop will at worst case execute 32 times. So, TC O(1).
    # We do the operation n & (n-1) every iteration and increment res. The operation n & (n-1) will eliminate one 1
    # every iteration and it will work one the same number of times as there are number of 1`s in n.`
        res = 0

        while n:
            res += 1
            n = n & (n-1)
        
        return res

#Testcases:
n = 0b00000000000000000000000000001011
print(Solution().hammingWeight(n))

n = 0b00000000000000000000000010000000
print(Solution().hammingWeight(n))

n = 0b11111111111111111111111111111101
print(Solution().hammingWeight(n))