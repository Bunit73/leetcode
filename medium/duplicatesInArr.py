# https://leetcode.com/problems/find-all-duplicates-in-an-array/#/description
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_hash = {}
        dup_arr = []
        
        for x in nums:
            if x in num_hash:
                dup_arr.append(x)
            else:
                num_hash[x] = 1
        return dup_arr
