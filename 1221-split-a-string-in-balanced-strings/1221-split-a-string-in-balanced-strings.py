class Solution:
    def balancedStringSplit(self, s: str) -> int:
        pointer = 0

        L = 0
        R = 0
        count = 0
        
        while pointer < len(s):
            if s[pointer] == "L":
                L += 1
            else:
                R += 1
            if L == R:
                count += 1
                L, R = 0, 0
            pointer += 1
            
        return count