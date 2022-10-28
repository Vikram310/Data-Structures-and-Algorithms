class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return 
        
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value
            
            if remaining in seen:
                return [seen[remaining],i]
            else:
                seen[value] = i