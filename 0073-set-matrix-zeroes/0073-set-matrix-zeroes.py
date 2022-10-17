class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        Firstrow = False
        
        #Find in which row n column do we have zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i >0:
                        matrix[i][0] = 0
                    else:
                        Firstrow = True
        
        #Fill rows and columns apart from first with zeroes wherever required
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
        #Fill first column
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0
        
        # Fill first row
        if Firstrow:
            for j in range(n):
                matrix[0][j] = 0
        
        