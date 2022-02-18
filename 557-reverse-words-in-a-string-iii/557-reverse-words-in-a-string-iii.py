class Solution:
    def reverseWords(self, s: str) -> str:    
        # so that last word also is reversed
        s = s + " "
        l,r = 0, 0

        string = ""

        while r < len(s):
            if s[r] != " ":
                r += 1
            elif s[r] == " ":
                string = string + s[l:r][::-1]
                string = string + " "
                r += 1
                l = r
        
        # extra space appended being removed here
        return string[:-1]

       
    def personal():   
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
            
        
        