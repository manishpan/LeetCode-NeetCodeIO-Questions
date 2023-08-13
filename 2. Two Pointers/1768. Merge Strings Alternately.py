#Problem statement: You are given two strings word1 and word2. Merge the strings by adding letters in alternating
#order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the
#merged string.

#Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
    #We store our result in mergedString, initializes indices to word1 and word2 in i, j.
        mergedString = ""
        i, j = 0, 0
        len_word1, len_word2 = len(word1), len(word2)

    #We start merging one character from word1 and then from word2 while keep checking if either i or j or both has
    # reached the end of string.
        while i < len_word1 and j < len_word2:
            mergedString += word1[i]
            i += 1
            mergedString += word2[j]
            j += 1

    #If entire word2 has been exhausted and word1 has some characters left, we append it to mergeString.
        while i < len_word1:
            mergedString += word1[i]
            i += 1

    #If entire word1 has been exhausted and word2 has some characters left, we append it to mergeString.
        while j < len_word2:
            mergedString += word2[j]
            j += 1

        return mergedString

#Testcases:
word1 = "abc"
word2 = "pqr"
print(Solution().mergeAlternately(word1, word2))

word1 = "ab"
word2 = "pqrs"
print(Solution().mergeAlternately(word1, word2))

word1 = "abcd"
word2 = "pq"
print(Solution().mergeAlternately(word1, word2))