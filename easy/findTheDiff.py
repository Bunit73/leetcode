# https://leetcode.com/problems/find-the-difference/#/description
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
    
        
        for c in xrange(len(t)):
            if c >= len(s):
                return t[c]
            if t[c] != s[c]:
                return t[c]
