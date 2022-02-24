class Solution:
    def removeDuplicates(self, s: str) -> str:
        s_l = list(s)

        stack = []

        for i in s_l:
            if len(stack) > 0 and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        
        return "".join(stack)