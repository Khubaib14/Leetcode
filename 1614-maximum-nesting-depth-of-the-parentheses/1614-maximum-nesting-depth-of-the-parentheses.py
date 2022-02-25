class Solution:
    def maxDepth(self, s: str) -> int:
        stack, count = [], 0
        for i in s:
            if i == "(":
                stack.append(i)
                if len(stack) > count:
                    count = len(stack)
            elif stack and i == ")":
                stack.pop()

        return count
