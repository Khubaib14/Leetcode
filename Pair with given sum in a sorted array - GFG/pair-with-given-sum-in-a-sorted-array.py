#User function Template for python3


class Solution:
    def Countpair (self, arr, n, k) : 
        #Complete the function
        l = 0 
        h = n-1 
        count = 0
        while l < h:
    
            if arr[l] + arr[h] == K:
                count +=1 
                l += 1 
                h -=1 
            elif arr[l] + arr[h] < K:
                l += 1 
            elif arr[l] + arr[h] > K:
                h -= 1 
            
        if count == 0:
            return -1
        return count


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    K = int(input())
    res = Solution().Countpair(arr, n, K)
    print(res)



# } Driver Code Ends