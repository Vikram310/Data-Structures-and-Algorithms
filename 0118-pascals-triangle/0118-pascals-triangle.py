class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = [[1]*i for i in range(1, numRows+1)]   # initialize triangle with all 1
        for i in range(1, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1] # update each as sum of two elements from above row
        return ans