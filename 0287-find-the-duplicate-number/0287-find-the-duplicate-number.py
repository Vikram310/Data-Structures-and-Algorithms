class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        low = 1
        high = len(nums) - 1
        
        while low < high:
            mid = (low+high) // 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
                
            if count <= mid:
                low = mid+1
            else:
                high = mid
                
        return low