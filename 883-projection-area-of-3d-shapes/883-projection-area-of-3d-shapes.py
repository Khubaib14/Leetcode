class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        total = 0
        
        # top
        cnt = 0
        c = len(grid[0])
        for i in range(c*c):
            if grid[i//c][i%c] == 0:
                cnt += 1
        total += (len(grid)*len(grid[0]) - cnt)
        
        # front
        total +=  sum([max(col) for col in zip(*grid)])
        
        # side
        total +=  sum([max(row) for row in grid])
        return total