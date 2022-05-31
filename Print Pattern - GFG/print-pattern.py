#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    
    # Below is the code I 
    # came up with in my first 
    # attempt. The recursive depth
    # is hit here.

    def dec(self, n, ls):
        if n <= 0:
            ls.append(n)
            return ls
        ls.append(n)
        n -= 5
        self.dec(n, ls)
        return ls
        
    def inc(self, n, ls, N):
        if n == N:
            return ls
        n += 5
        ls.append(n)
        self.inc(n, ls, N)
        return ls
    
    
    def pattern(self, n):
        # code here
        N = n
        ls = []
        self.dec(n, ls)
        self.inc(ls[-1], ls, N)
        return ls
        
    
    # def pattern(self, n):
    #     pass
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends