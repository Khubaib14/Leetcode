class Solution:
    def findMaxSubarraySum(self, arr, n, x):
        # Your code goes here
        
        slow = 0
        fast = 0
        total = 0
        maxer = 0
        
        while fast < len(arr):
            total += arr[fast]
            if total <= x:
                maxer = max(maxer, total)
                # print(arr[slow: fast+1])
            elif total > x:
                while total > x:
                    total -= arr[slow]
                    slow += 1
                if total <= x:
                    maxer = max(maxer, total)
                    # print(arr[slow: fast+1])
            fast += 1
        return (maxer)
#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a=list(map(int,input().split()))
        k = int(input())
        ob = Solution()
        ans=ob.findMaxSubarraySum(a,n,k)
        print(ans)

# } Driver Code Ends