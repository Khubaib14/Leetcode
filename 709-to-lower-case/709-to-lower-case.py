class Solution:
    def toLowerCase(self, s: str) -> str:
        l = list(s)
        for i in range(len(s)):
            char = ord(l[i])
            if char in range(65, 91):
                l[i] = chr(char + 32)
            else:
                pass
        return "".join(l) 