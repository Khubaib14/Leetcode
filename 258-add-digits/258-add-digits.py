class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            x  = num % 9
            if x == 0:
                return 9
            else:
                return x
        