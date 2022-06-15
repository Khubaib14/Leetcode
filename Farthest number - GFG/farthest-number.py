#User function Template for python3

class Solution:
    def SuffixArrayOfMin(self, arr):
        suffix_arr = [0]*len(arr)
        suffix_arr[-1] = arr[-1]
        
        for i in range(len(arr)-1, 0, -1):
            suffix_arr[i - 1] = min(arr[i-1], suffix_arr[i])
    
        return suffix_arr

    def BinarySearchInSuffixArray(self, arr):
        result = []
        suffix_arr = self.SuffixArrayOfMin(arr)
        for i in range(len(arr)):
            start = i + 1
            end = len(arr) - 1
            ans = -1
            while start <= end:
                mid = (start + end)//2
                if suffix_arr[mid] < arr[i]:
                    ans = mid
                    start = mid + 1
                else:
                    end = mid - 1 
            result.append(ans)
        return result

    def farNumber(self,N,Arr):
        #code here
        return self.BinarySearchInSuffixArray(Arr)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        N=int(input())
        Arr=[int(x) for x in input().split()]
        
        ob = Solution()
        ans = ob.farNumber(N,Arr)
        
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends