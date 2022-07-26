class Solution:
    def construct2DArray(self, mat: List[int], m: int, n: int) -> List[List[int]]:
        #n = len(mat)
        #m = len(mat[0])
        #if n*m != r*c:
        #    return mat
        #else:
        #flat = self.Flatten(mat)
        if n*m == len(mat):
            newmat = []
            cnt = 0
            for _ in range(m):
                temp = []
                for _ in range(n):
                    temp.append(mat[cnt])
                    cnt += 1
                newmat.append(temp)
            return newmat
        else:
            return []