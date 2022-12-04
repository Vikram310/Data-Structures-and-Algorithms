class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        sum_start, sum_end, res, diff, n = 0,0,0,1e9,len(nums)
        
        for i in range(n):
            sum_end += nums[i]
            
        for i in range(n):
            sum_start += nums[i]
            sum_end -= nums[i]
            
            avg1 = sum_start // (i+1)
            avg2 = sum_end // (n-i-1) if i != n-1 else 0
            
            if abs(avg1 - avg2) < diff:
                diff = abs(avg1-avg2)
                res = i
            
        return res
        
        