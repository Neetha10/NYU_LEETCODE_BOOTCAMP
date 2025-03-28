class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        row_flag=False
        col_flag=False
        for i in range (m):
            if matrix[i][0]==0:
                col_flag=True
                break
        for j in range (n):
            if matrix[0][j]==0:
                row_flag=True
                break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        if row_flag:
            for j in range(n):
                matrix[0][j]=0
        
        if col_flag:
            for i in range(m):
                matrix[i][0]=0

        """
        Do not return anything, modify matrix in-place instead.
        """
        