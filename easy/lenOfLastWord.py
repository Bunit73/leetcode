# https://leetcode.com/problems/length-of-last-word/#/discuss
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        
        word_list = s.split(" ")
        
        for w in reversed(word_list):
            if w != '':
                return len(w)
        
        return 0
