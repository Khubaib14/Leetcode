class Solution:
    def getmaxofcol(self, mat, c):
        r = len(mat) #3
        most = -1
        for i in range(r):
            if mat[i][c] > most:
                most = mat[i][c]
        return most
    
    
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minrow = set(min(r) for r in matrix)
        maxcol = set(max(c) for c in zip(*matrix))
        return (minrow&maxcol)
        
        
        
        
        
    def solOne(self, matrix):
        # this solution throws some internal Leetcode error
        r = len(matrix) #3
        c = len(matrix[0]) #4
        for i in range(r):
            least = 99999
            col_check = -1
            for j in range(c):
                if matrix[i][j] < least:
                    least = matrix[i][j]
                    col_check = j
            if self.getmaxofcol(matrix, col_check) == least:
                return least