class Solution:
    def fib(self, n: int) -> int:
        
        def dfs(n):
            
            if n<2:
                return n
            return dfs(n-1) + dfs(n-2)
        return dfs(n)