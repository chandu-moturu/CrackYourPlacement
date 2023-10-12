class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        index=[]
        row=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] == 0):
                    index.append(j)
                    row.append(i)
      
        for i in range(len(matrix)):
            for j in index:
                matrix[i][j]=0
        
        for i in row:
            matrix[i]=[0]*len(matrix[i])
                