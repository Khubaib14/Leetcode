#User function Template for python3

class Solution:
    def BinarySearch(self, arr, k): # arr = arr2
        start = 0
        end = len(arr) - 1
        mid = (start + end)//2
        while start <= end:
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end)//2        
        return False
        
    
    def isKSortedArray(self, arr, n, k): 
        #code here.
        arr2 = sorted(arr)
        for i in range(len(arr)):
            if abs(i - self.BinarySearch(arr2, arr[i])) > k:
                return "No"
        return "Yes"

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    ob = Solution()
    print(ob.isKSortedArray(a, n, k))

# } Driver Code Ends