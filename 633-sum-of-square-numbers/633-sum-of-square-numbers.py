class Solution:
    def Sqrt(self, num):
        start = 0
        end = num
        while start <= end:
            mid = (start + end)//2
            sq = mid * mid
            if sq == num:
                return mid
            elif sq > num:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    
    def solOne(self, c):
        if c == 0:
            return True
        for i in range(c):
            numtocheck = c - i**2
            sqrt = self.Sqrt(numtocheck)
            if sqrt != -1:
                return True
        return False
    
    def judgeSquareSum(self, c: int) -> bool:
        l=0 ; r=int(sqrt(c))
        while l<=r:
            s=l**2+r**2
            if s>c: r-=1
            elif s<c: l+=1
            else: return True
        
        
        
        
        
        
        
        