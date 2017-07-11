# https://leetcode.com/problems/student-attendance-record-i/#/description
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent_count = 0
        late_count = 0
        
        for c in xrange(len(s)):
            if s[c] == 'A':
                absent_count += 1
                late_count = 0
                
            elif s[c] == 'L':
                late_count += 1
            
            else:
                late_count = 0
            
            if absent_count > 1 or late_count > 2:
                return False
        return True
