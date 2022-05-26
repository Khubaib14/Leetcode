#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def MakeDict(self, s):
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        return d
    
    def isAnagram(self,a,b):
        if self.MakeDict(a) == self.MakeDict(b):
            return "YES"
        else:
            "NO"

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends