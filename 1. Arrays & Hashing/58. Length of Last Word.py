#Problem statement: Given a string s consisting of words and spaces, return the length of the last word in the
#string.

#A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s):
    count = 0
    i = len(s) - 1
    while s[i] == ' ':
        i = i - 1
    while i > -1 and s[i] != ' ' :
        count = count + 1
        i = i - 1
    return count

s = "luffy is still joyboy"
print(lengthOfLastWord(s))

s = "joyboy"
print(lengthOfLastWord(s))

s = " fly me to the moon  "
print(lengthOfLastWord(s))