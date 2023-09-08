#Problem Statement: Reverse bits of a given 32 bits unsigned integer.

class Solution:
    def reverseBits(self, n):
    #We take res =0 , shift it right by 1 place and add last bit of n (by using n & 1) and shift n by 1.
        res = 0

        for i in range(32):
            res = res << 1
            res = res | (n & 1)
            n = n >> 1
        
        return n

#Testcases:
n = 00000010100101000001111010011100
print(Solution().reverseBits(n))

n = 11111111111111111111111111111101
print(Solution().reverseBits(n))