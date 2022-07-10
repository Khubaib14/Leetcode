class Solution:
    def Flatten(self, mat):
        result = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                result.append(mat[i][j])
        return result
    
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if n*m != r*c:
            return mat
        else:
            flat = self.Flatten(mat)
            newmat = []
            cnt = 0
            for _ in range(r):
                temp = []
                for _ in range(c):
                    temp.append(flat[cnt])
                    cnt += 1
                newmat.append(temp)
            return newmat