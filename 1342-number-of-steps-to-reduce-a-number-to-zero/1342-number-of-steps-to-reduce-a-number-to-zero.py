class Solution:
    def Solve(self, n, cnt):
        if n == 0:
            return cnt
        if n % 2 == 0:
            return self.Solve(n//2, cnt+1)
        else:
            return self.Solve(n-1, cnt+1)
    
    
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        return self.Solve(num, cnt)
        
 
    def solOne(self, num):
        # First attempt
        count = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
                count += 1
            else:
                num -= 1
                count += 1
        return count