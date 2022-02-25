class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stacker(string):
            stack = []
            for i in string:
                if stack and i == "#":
                    stack.pop()
                else:
                    if i != "#":
                        stack.append(i)
            return "".join(stack)
        
        stack_c = stacker(s)
        stack_t = stacker(t)
        
        if stack_c == stack_t:
            return True
        
        return False

    
        