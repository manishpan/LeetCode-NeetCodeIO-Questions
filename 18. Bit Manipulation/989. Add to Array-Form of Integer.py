#Problem Statement: The array-form of an integer num is an array representing its digits in left to right order.

#For example, for num = 1321, the array form is [1,3,2,1].
#Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

class Solution:
    def addToArrayForm(self, num, k: int):
        num.reverse()
        i = 0

        while k:
            digit = k % 10
            if i < len(num):
                num[i] += digit
            else:
                num.append(digit)

            carry = num[i] // 10
            num[i] = num[i] % 10

            k //= 10
            k += carry
            i += 1
        
        num.reverse()
        return num

#Testcases:
num = [1,2,0,0]
k = 34
print(Solution().addToArrayForm(num, k))

num = [2,7,4]
k = 181
print(Solution().addToArrayForm(num, k))

num = [2,1,5]
k = 806
print(Solution().addToArrayForm(num, k))

num = [9,9,9,9,9,9,9,9,9,9]
k = 1
print(Solution().addToArrayForm(num, k))

num = [7]
k = 93
print(Solution().addToArrayForm(num, k))