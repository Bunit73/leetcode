class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Brute force solutuion
        for x in xrange(0,len(nums)):
            for y in xrange(len(nums)-1,x,-1):
                if nums[x] + nums[y] == target:
                    return [x,y]
            
