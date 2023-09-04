#Problem Statement: You are given a large integer represented as an integer array digits, where each digits[i] is the
# ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits):
    #We traverse the array from the end, if end digit is 9, we make it 0 and decrement i pointer by 1. We keep on 
    # changing digit to digit + 1 unless we encounter a number which is less than 9. In that case, we add 1 to digit
    # and return digits array.
        n = len(digits)
        i = n - 1

        while i > -1:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1
        
        return [1] + digits #Denotes carry

#Testcases:
digits = [1,2,3]
print(Solution().plusOne(digits))

digits = [4,3,2,1]
print(Solution().plusOne(digits))

digits = [9]
print(Solution().plusOne(digits))