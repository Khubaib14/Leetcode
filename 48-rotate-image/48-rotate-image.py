class Solution:
    def Transpose(self, mat):
        transpose = []
        for i in zip(*mat):
            transpose.append(list(i))
        return transpose
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # reverse
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # transpose 
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        def solOne(self, mat):
            mat = self.Transpose(mat)
            for i in range(len(mat)):
                for j in range(len(mat)//2):
                    mat[i][j], mat[i][len(mat)-j-1] = mat[i][len(mat)-j-1], mat[i][j]
            return mat
        