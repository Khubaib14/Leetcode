class Solution:
    def maxDepth(self, s: str) -> int:
        pointer = 0
        count = 0
        maximum = 0
        while pointer < len(s):
            if s[pointer] == "(":
                count += 1
                maximum = max(count, maximum)
            elif s[pointer] == ")":
                count -= 1
            pointer += 1

        return maximum
        
        
        
        
        
        
        stack, count = [], 0
        for i in s:
            if i == "(":
                stack.append(i)
                if len(stack) > count:
                    count = len(stack)
            elif stack and i == ")":
                stack.pop()

        return count
