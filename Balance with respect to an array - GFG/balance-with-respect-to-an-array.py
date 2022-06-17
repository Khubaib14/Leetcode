#User function Template for python3

class Solution:
    def Floor(self, arr, target):
        start = 0
        end = len(arr) - 1
        ans = -1
        while start <= end:
            mid = (start + end)//2
            if arr[mid] < target:
                ans = mid
                start = mid + 1
            elif arr[mid] > target:
                end = mid - 1
            elif arr[mid] == target:
                return mid
        return ans
    
    def Ceiling(self, arr, target):
        start = 0
        end = len(arr) - 1
        ans = -1
        while start <= end:
            mid = (start + end)//2
            if arr[mid] < target:
                start = mid + 1
            elif arr[mid] > target:
                ans = mid
                end = mid - 1
            elif arr[mid] == target:
                return mid
        return ans
    
    
    
    def isBalanced(self,arr,n,target):
        floor_index = self.Floor(arr, target)
        ceil_index = self.Ceiling(arr, target)
        
        if floor_index == -1 or ceil_index == -1:
            return "Balanced"
        
        floor = arr[floor_index]
        ceiling = arr[ceil_index]
        if abs(target - floor) == abs(ceiling - target):
            return "Balanced"
        else:
            return "Not Balanced"

#{ 
#  Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    x=int(input())
    ob=Solution()
    print(ob.isBalanced(a,n,x))


# } Driver Code Ends