class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        res = [] #initialise result array
        total = 0 # total sum of nums
        
        for i in range(len(nums)):
            total += nums[i]
        
        '''
        sum_start = sum from starting to ith index
        sum_end = sum from end to (i+1)th index
        '''
        n = len(nums)
        sum_start, sum_end = 0, total
        for i in range(len(nums)):
            sum_start += nums[i]  
            sum_end -= nums[i]
            avg_start = (sum_start // float((i+1)))
            if i == n-1:
                avg_end = 0
            else:
                avg_end = (sum_end // float((n-i-1))) if i != n-1 else 0
            #print(avg_start,avg_end)
            avg = avg_start - avg_end if avg_start > avg_end else avg_end-avg_start
            res.append(avg)

        return res.index(min(res))
            