#https://leetcode.com/problems/max-consecutive-ones/#/description
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        con = 0
        max_con = 0
        last_check = False
        
        for x in nums:
            if x == 1:
                if last_check:
                    con += 1
                else:
                    con = 1
                    last_check = True
                if con > max_con:
                    max_con = con
            else:
                last_check = False
                con = 0
        return max_con
