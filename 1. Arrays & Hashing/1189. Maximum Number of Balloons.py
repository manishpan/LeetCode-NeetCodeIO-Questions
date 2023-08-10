#Problem statement: Given a string text, you want to use the characters of text to form as many instances of the
#word "balloon" as possible.

#You can use each character in text at most once. Return the maximum number of instances that can be formed.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
    #Creating a dictionary to maintain counts of letters 'b', 'a', 'l', 'o', 'n'
        count_dict = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}

    #Count the occurences of 'b', 'a', 'l', 'o', 'n' in text.
        for i in text:
            if i in count_dict:
                count_dict[i] += 1

    #The max_instances of balloon will be the min count in count_dict. 2 l`s and 2o`s are counted in 1 instance.
    #Hence dividing the count of l and o by 2.
        count_dict['l'] //= 2
        count_dict['o'] //= 2
    
        return min(count_dict.values())
    
#Testcases:
text = "nlaebolko"
print(Solution().maxNumberOfBalloons(text))

text = "loonbalxballpoon"
print(Solution().maxNumberOfBalloons(text))

text = "leetcode"
print(Solution().maxNumberOfBalloons(text))