class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
    
        for i in s:
            if len(stack) > 0 and ((ord(i) - ord(stack[-1]) == 32) or (ord(stack[-1]) - ord(i) == 32)):
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)
        