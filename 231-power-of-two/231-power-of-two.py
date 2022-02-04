class Solution:
    def isPowerOfTwo(self, x: int) -> bool:
        if x <= 0:
            return False
        while x > 1:
            x = x / 2
            if x%1 != 0:
                return False
                break
        return True
            
