class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stk = []
        res = 0
        
        for op in ops:
            if op == 'C':
                res -= stk.pop()
            elif op == 'D':
                stk.append(stk[-1]*2)
                res += stk[-1]
            elif op == '+':
                stk.append(stk[-1]+stk[-2])
                res += stk[-1]
            else:
                stk.append(int(op))
                res += stk[-1]
                    
        return res
        
        
        
        
        
        
        
        
    def solOne(self, ops):
        history = []
        for op in ops:
            if op == 'C':
                history.pop()
            elif op == 'D':
                history.append(history[-1] * 2)
            elif op == '+':
                history.append(history[-1] + history[-2])
            else:
                history.append(int(op))
        return sum(history)