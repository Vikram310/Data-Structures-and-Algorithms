class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0 or x == 1:
            return x
        
        start = 1
        end = x
        
        while start <= end:
            mid = (start+end) // 2
            mid_sq = mid*mid
            if mid_sq == x:
                return mid
            if mid_sq < x:
                start = mid+1
                ans = mid
            else:
                end = mid-1
            
        return ans
        