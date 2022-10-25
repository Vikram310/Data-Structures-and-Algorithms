class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #initialise a hash map 
        count = {}
        res, maxCount = 0, 0 
        
        for n in nums:
            count[n] = 1 + count.get(n,0)
            res = n if count[n] > maxCount else res 
            maxCount = max(count[n],maxCount)
        return res 
        
        