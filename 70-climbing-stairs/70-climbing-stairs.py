class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dfs(n):
            if n ==1 :
                return 1
            if n == 2: 
                return 2
            return dfs(n-1) + dfs(n-2)
        return dfs(n)