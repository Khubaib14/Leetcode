class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s)-1:
            if s[i] == s[i+1]:
                i += 1
            elif s[i].lower() == s[i+1] or s[i].upper() == s[i+1]:
                s = s[:i] + s[i+2:]
                i = 0
            else:
                i += 1
        
        return s
    
    
        
    def firstOne(self, s: str):    
        stack = []
    
        for i in s:
            if stack and ((ord(i) - ord(stack[-1]) == 32) or (ord(stack[-1]) - ord(i) == 32)):
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)
        