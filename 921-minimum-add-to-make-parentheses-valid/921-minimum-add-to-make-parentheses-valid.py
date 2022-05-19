class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        leftneed = 0
        rightneed = 0

        for i in s:
            if i == "(":
                rightneed += 1
            elif i == ")" and rightneed > 0:
                rightneed -= 1
            elif i == ")" and rightneed == 0:
                leftneed += 1


        return (rightneed + leftneed)

            
        
    def solOne(s):
        stack = []
        count = 0

        for i in s:
            if i == '(':
                stack.append("(")
            elif i == ')':
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    count += 1

        return (count+len(stack))

        