"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        sorted_array=sorted(strs)
        first_word = sorted_array[0]
        last_word = sorted_array[-1]
        sub_string = ''
        for i in range(min(len(first_word), len(last_word))):
            if first_word[i] != last_word[i]:
                return sub_string
            sub_string += first_word[i]
        return sub_string    
