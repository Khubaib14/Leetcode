#User function Template for python3

class Solution:
    def sumOfDigit(self, K):
        sod = 0
        while (K):
            sod =sod + K % 10
            K = K // 10
        return sod
    
    def getCount(self, n , diff):
        # code here 
        low = 1
        high = n
     
        # binary search while loop   
        while (low <= high):
         
            mid = (low + high) // 2
     
            if (mid - self.sumOfDigit(mid) < diff):       
                low = mid + 1   
            else:
                 
                high = mid - 1       
         
     
        return (n- high)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,D=map(int,input().split())
        
        ob = Solution()
        print(ob.getCount(N, D))
# } Driver Code Ends