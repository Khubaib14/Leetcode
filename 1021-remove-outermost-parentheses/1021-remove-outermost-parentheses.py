class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        stk = []
        curr = 0
        for i in range(len(s)):
            if s[i] == "(":
                stk.append(s[i])
            elif s[i] == ")" and not stk:
                return None
            elif s[i] == ')' and stk:
                stk.pop()
            if len(stk) == 0:
                result.append(s[curr+1:i])
                curr = i+1
        return "".join(result)