class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        frow=False
        fcol=False
        for j in range(n):
            if matrix[0][j]==0:
                frow=True
                break
        for i in range(m):
            if matrix[i][0]==0:
                fcol=True
                break
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if frow:
            for j in range(n):
                matrix[0][j]=0
        if fcol:
            for i in range(m):
                matrix[i][0]=0
        return matrix