class Solution:
    def balancedStringSplit(self, s: str) -> int:
        pointer = 0
        count = 0
        chk = 0

        while pointer < len(s):
            if s[pointer] == "L":
                chk -= 1
            else:
                chk += 1
            if chk == 0:
                count += 1
            pointer += 1

        return count
        
        
    def solution1(s):    
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