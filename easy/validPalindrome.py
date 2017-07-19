# https://leetcode.com/submissions/detail/110316063/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s == '':
            return True
        
        letterStack = []
        
        for x in xrange(len(s)):
            if s[x].isalnum():
                letterStack.append(s[x])
        
        for x in xrange(len(letterStack)/2):
            if (letterStack[x].lower() != letterStack[len(letterStack)-x-1].lower()):
                return False
            
        return True
