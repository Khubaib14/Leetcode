#User function Template for python3

class Solution:
    def Solve(self, ip, op=[], mix=[]):
        if len(ip) == 0:
            mix.append(op)
            return
        
        op1 = op[:]
        op2 = op[:]
        
        op2.append(ip[0])
        ip = ip[1:]
        
        self.Solve(ip, op1, mix)
        self.Solve(ip, op2, mix)
        
        return mix
    
    def subsets(self, A):
        #code here
        mix = []
        self.Solve(A, [], mix)
        mix.sort()
        return mix

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends