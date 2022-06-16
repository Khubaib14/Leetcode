#User function Template for python3
import bisect as bt
# hs to use this 
class Solution:
    def MaxBoundBinarySearch(self, arr, target):
        start = 0
        end = len(arr) - 1
        ans = -1
        while start <= end:
            mid = (start + end)//2
            if arr[mid] > target:
                end = mid - 1
            elif arr[mid] <= target:
                ans = mid
                start = mid + 1
        return ans
    
    
    
    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        #returns the required output
        arr2.sort()
        res = []
        for e in arr1:
           res.append(bt.bisect(arr2,e))
           
        return res
        """
        result = []
        arr2.sort()
        for i in arr1:
            result.append(self.MaxBoundBinarySearch(arr2, i)+1)
        return result
        """

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1,n2=[int(x) for x in input().split()]
        arr1=[int(x) for x in input().split()]
        arr2=[int(x) for x in input().split()]
    
        res = Solution().countEleLessThanOrEqual(arr1,n1,arr2,n2)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends