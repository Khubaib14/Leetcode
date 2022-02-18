class Solution:
    def reverseWords(self, s: str) -> str:    
        def reverser(s):
            """reverses string"""
            q = list(s)
            l,r = 0, len(q) - 1
            while l<=r:
                q[l], q[r] = q[r], q[l]
                l += 1
                r -= 1
            return "".join(q)
        
        l = list(s.split(" "))
        
        for i in range(len(l)):
            l[i] = reverser(l[i])

        return " ".join(l)
            
        
        