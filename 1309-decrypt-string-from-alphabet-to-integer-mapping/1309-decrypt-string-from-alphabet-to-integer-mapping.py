class Solution:
    def alpha(self, num):
        return chr(int(num) + ord('a') - 1)
    
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = []
        
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                ans.append(self.alpha(s[i:i+2]))
                i += 3
            else:
                ans.append(self.alpha(s[i]))
                i += 1
        
        return ''.join(ans)