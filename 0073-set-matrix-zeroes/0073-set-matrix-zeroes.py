class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        Firstrow = False
        
        #Find in which row n column do we have zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r >0:
                        matrix[r][0] = 0
                    else:
                        Firstrow = True
        
        #Fill rows and columns apart from first with zeroes wherever required
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        #Fill first column
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        # Fill first row
        if Firstrow:
            for c in range(cols):
                matrix[0][c] = 0
        
        