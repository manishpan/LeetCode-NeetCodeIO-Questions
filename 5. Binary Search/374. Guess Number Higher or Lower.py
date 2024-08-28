#Problem Statement: We are playing the Guess Game. The game is as follows:

#I pick a number from 1 to n. You have to guess which number I picked.

#Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

#You call a pre-defined API int guess(int num), which returns three possible results:

#-1: Your guess is higher than the number I picked (i.e. num > pick).
#1: Your guess is lower than the number I picked (i.e. num < pick).
#0: your guess is equal to the number I picked (i.e. num == pick).
#Return the number that I picked.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guess(self, num):
        if num > pick:
            return -1
        elif num < pick:
            return 1
        return 0

    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while True:
            num = (l + r) // 2
            res = self.guess(num)
            if res == 1:
                l = num + 1
            elif res == -1:
                r = num - 1
            else:
                return num

#Testcases:
n = 10
pick = 6
print(Solution().guessNumber(n))

n = 1
pick = 1
print(Solution().guessNumber(n))

n = 2
pick = 1
print(Solution().guessNumber(n))