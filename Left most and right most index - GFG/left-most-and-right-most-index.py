#User function Template for python3

class Solution:
    def BinarySearchLowest(self, arr, k):
        start = 0
        end = len(arr) - 1
        mid = (start + end)//2
        cnt = -1
        
        while start <= end:
            if arr[mid] == k:
                cnt = mid
                end = mid - 1
            elif arr[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end)//2
        return cnt
    
    
    def BinarySearchHighest(self, arr, k):
        start = 0
        end = len(arr) - 1
        mid = (start + end)//2
        cnt = -1
        
        while start <= end:
            if arr[mid] == k:
                cnt = mid
                start = mid + 1
            elif arr[mid] < k:
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end)//2
        return cnt
    
    
    
    def indexes(self, v, x):
        # Your code goes here
        lowest = self.BinarySearchLowest(v, x)
        highest = self.BinarySearchHighest(v,x) 
        
        return lowest, highest 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends