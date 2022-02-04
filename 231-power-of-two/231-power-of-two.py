class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            if n == 1:
                return True
            elif n%1 == 0:
                return self.isPowerOfTwo(n/2)
            else:
                return False
            
