#User function Template for python3
class Solution:
    def maximumSumSubarray (self,k,s,N):
        # code here 
        slow = 0
        fast = 0
        maxer = 0
        total = 0
        
        while fast < len(s):
            total += s[fast]
            if fast - slow + 1 < k:
                fast += 1
            elif fast - slow + 1 == k:
                maxer = max(maxer, total)
                # print(maxer, s[slow: fast+1])
                total -= s[slow]
                slow += 1
                fast += 1
            
        return (maxer)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends