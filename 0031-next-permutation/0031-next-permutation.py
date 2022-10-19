class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        
        #length <= 2
        if length <=2:
            return nums.reverse()
        
        # pointer at last but 1 poisition to find the pattern
        pointer = length - 2
        
        # finding the poistion at which the desceding order pattern is stopped 
        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1
        
        if pointer == -1:
            return nums.reverse()
            
        for x in range(length - 1,pointer,-1):
            if nums[pointer] < nums[x]:
                nums[pointer],nums[x] = nums[x],nums[pointer]
                break
        
        nums[pointer+1:] = reversed(nums[pointer+1:])
        