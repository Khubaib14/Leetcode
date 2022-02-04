class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            if n == 1:
                return True
            elif n%1 == 0:
                return self.isPowerOfThree(n/3)
            else:
                return False