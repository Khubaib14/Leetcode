#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, k):
        #Your code here
        start = 0
        end = len(arr) - 1
        mid = (start + end)//2
        
        while start <= end:
            if arr[mid] == k:
                return 1
            elif arr[mid] < k:
                start = mid + 1
            else:
                end = mid - 1
                
            mid = (start + end)//2
        
        return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		NK = input().strip().split()
		N = int(NK[0])
		K = int(NK[1])
		A = [ int(x) for x in input().strip().split() ]
		ob=Solution()
		print(ob.searchInSorted(A,N,K))

# } Driver Code Ends