#User function Template for python3

class Solution:
    def Decode(self, stk):
        temp = ""
        while stk:
            temp += stk[-1][0]
            stk.pop()
        return temp[::-1]
    
    
    def Reduced_String(self, k, s):
        # Your code goes here
        # return the reduced string
        if k == 1:
            return ""
        elif k == 0:
            return s
        stk = []
        for i in s:
            if not stk:
                stk.append((i,1))
            elif stk and stk[-1][0] == i:
                stk.append((i, stk[-1][1] + 1))
                if stk[-1][1] == k:
                    while stk and stk[-1][0] == i and stk[-1][1] <= k:
                        stk.pop()
            elif stk and stk[-1][0] != i:
                stk.append((i, 1))
        return self.Decode(stk)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        k=int(input())
        s=input().strip()
        obj = Solution()
        print(obj.Reduced_String(k,s))

# } Driver Code Ends