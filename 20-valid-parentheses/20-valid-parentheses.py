class Solution:
    def isValid(self, s: str) -> bool:
        opener = []
        for i in s:
            if i == "[" or i == "(" or i == "{":
                opener.append(i)
            if len(opener) > 0:
                if i == "]": 
                    if opener[-1] == '[':
                        opener.pop()
                    else:
                        return False
                elif i == "}": 
                    if opener[-1] == '{':
                        opener.pop()
                    else:
                        return False
                elif i == ")": 
                    if opener[-1] == '(':
                        opener.pop()
                    else:
                        return False
            else:
                return False
        if len(opener) == 0:
            return True
        else:
            return False