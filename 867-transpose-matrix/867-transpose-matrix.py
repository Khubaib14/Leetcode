class Solution:
    def getCol(self, matrix, col):
        temp = []
        r = len(matrix) # 2
        for i in range(r):
            temp.append(matrix[i][col])
        return temp
    
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix) # 2
        c = len(matrix[0]) # 3
        temp = []
        for i in range(c):
            temp.append(self.getCol(matrix, i))
        return temp