class Solution:
    def WoodCollected(self, arr, cutheight):
        total = 0
        for i in arr:
            if i > cutheight:
                total += (i - cutheight)
        return total
    
    def Search(self, arr, targetsum):
        start = 0
        end = arr[-1]
        while start <= end:
            mid = (start + end)//2
            amtwood = self.WoodCollected(arr, mid)
            if amtwood == targetsum:
                return mid
            elif amtwood > targetsum:
                start = mid + 1
            elif amtwood < targetsum:
                end = mid - 1
        return -1
    
    def find_height(self,arr,n,targetsum):
        # code here
        arr.sort()
        return self.Search(arr, targetsum)
    
    
#{ 
#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        tree = [ int(x) for x in input().strip().split() ]
        k = int(input())
        ob=Solution()
        print(ob.find_height(tree,n,k))
# } Driver Code Ends