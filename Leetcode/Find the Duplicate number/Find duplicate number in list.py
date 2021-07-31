#O(N) time and O(N) space
def findDuplicate(self,nums: list[int])->int:
    N = len(nums) - 1
    seen = [0]*(N+1)
    for num in nums:
        if seen[num]:
            return num
        seen[num] = 1

#bit manipulation
def findduplicate(nums: list[int])-> int:
    seen = 0
    for num in nums:
        if seen & (1 << num):
            return num
        seen |=  1 << num