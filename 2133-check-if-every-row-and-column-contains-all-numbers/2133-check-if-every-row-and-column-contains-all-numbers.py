class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i, j in zip(matrix, zip(*matrix)):
            if len(set(i)) != n or len(set(j)) != n:
                return False
        return True