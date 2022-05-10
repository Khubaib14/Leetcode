class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        fast, count1, max1, count0, max0 = 0,0,0,0,0

        while fast < len(s):
            if s[fast] == '1':
                count1 += 1
                count0 = 0
                max1 = max(count1, max1)
            elif s[fast] == '0':
                count0 += 1
                count1 = 0
                max0 = max(count0, max0)
            fast += 1
        
        if max1 > max0:
            return True
        else:
            return False

    