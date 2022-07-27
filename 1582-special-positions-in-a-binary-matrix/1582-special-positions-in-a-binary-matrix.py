class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = []
        cols = []
        cnt = 0
        for i in mat:
            rows.append(sum(i))
        for i in zip(*mat):
            cols.append(sum(i))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if rows[i] == cols[j] == mat[i][j] == 1:
                    cnt += 1
        return cnt