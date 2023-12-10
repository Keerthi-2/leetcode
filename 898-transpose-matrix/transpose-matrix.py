class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m=[[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m[j][i]=matrix[i][j]
                
        return m
                
        