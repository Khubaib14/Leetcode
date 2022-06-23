class Solution:
    def Solve(self, num1, num2, cnt):
        if num1 == 0 or num2 == 0:
            return cnt
        elif num1 >= num2:
            return self.Solve(num1-num2, num2, cnt+1)
        elif num1 < num2:
            return self.Solve(num1, num2-num1, cnt+1)
    
    
    def countOperations(self, num1: int, num2: int) -> int:
        cnt = 0
        return self.Solve(num1, num2, cnt)