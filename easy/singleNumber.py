# https://leetcode.com/problems/single-number/#/description
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        skip_next = False
        
        for i in xrange(0,len(nums)):
            if skip_next:
                skip_next = False
                
            else:
                if i == len(nums) - 1:
                    return nums[i]
                elif nums[i] == nums[i+1]:
                    skip_next = True
                else:
                    return nums[i]
