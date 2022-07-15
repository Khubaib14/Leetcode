#User function Template for python3

class Solution:
    def sumOfMatrix(self,N,M,Grid):
        #code here
        sum1=0
        for t in Grid:
            for k in range(0,M):
                sum1+=t[k]
    
        return sum1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(' '))
        Grid = [[0 for i in range(M)] for j in range(N)]
        for i in range(N):
            s=list(map(int,input().strip().split(' ')))
            for j in range(M):
                Grid[i][j]=s[j]
        ob=Solution()
        print(ob.sumOfMatrix(N,M,Grid)) 
# } Driver Code Ends