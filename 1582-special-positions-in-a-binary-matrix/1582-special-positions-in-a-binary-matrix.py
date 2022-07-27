class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = []
        cols = []
        cnt = 0
        
        # sum of row = 1 means only one 1
        for i in mat:
            rows.append(sum(i))
        
        # sum of col = 1 means only one 1
        for i in zip(*mat):
            cols.append(sum(i))
        
        # for pos where 1 is present 
        # see if that pos's rowsum and 
        # colsum is also 1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if rows[i] == cols[j] == mat[i][j] == 1:
                    cnt += 1
        return cnt