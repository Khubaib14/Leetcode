#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    
    def makeMap(self, arr):
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        return d
    
    def check(self,A,B,N):
        if self.makeMap(A) == self.makeMap(B):
            return True
        return False

        
        #code here
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends