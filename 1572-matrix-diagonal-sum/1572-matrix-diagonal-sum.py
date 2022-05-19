class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        first_sum = 0
        for i in range(len(mat[0])):
            other = (len(mat[0])) - i - 1
            first_sum += mat[i][i]
            if i != other:
                first_sum += mat[i][other]

        return (first_sum)
        
        
        
        
        
    def solOne(mat):    
        first_sum = 0
        second_sum = 0
        
        for i in range(len(mat[0])):
            first_sum += mat[i][i]

        for i in range(len(mat[0])):
            other = (len(mat[0])) - i - 1
            if i != other:
                second_sum += mat[i][other]

        return (second_sum + first_sum)