#User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        # code here 
        d = {}

        for i in arr:
            d[i] = d.get(i, 0) + 1
        
        for i in d:
            if d[i] == 1:
                return (i)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
# } Driver Code Ends