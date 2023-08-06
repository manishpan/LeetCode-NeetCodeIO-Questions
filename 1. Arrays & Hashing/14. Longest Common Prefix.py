#Problem statement: Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs) -> str:
    #Finding the length of smallest string in strs array
        min_str_len = min([len(s) for s in strs])
        prefix = ""

    #We pickup curr character and matches it with every string at same position. If character matches then we add it
    #prefix variable otherwise we return the prefix variable.
        for i in range(min_str_len):
            curr_char = strs[0][i]
            for str in strs:
                if curr_char != str[i]:
                    return prefix
            prefix += curr_char

    #If the above loop does not run even a single time we return prefix
        return prefix


#TestCases:
strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
print(Solution().longestCommonPrefix(strs))