#User function Template for python3


class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr, l, h):
        start = 0
        end = len(arr) - 1
        mid = (start + end)//2
        
        while start <= end:
            if arr[mid] > arr[end]:
                start = mid + 1
            elif arr[mid] < arr[start]:
                end = mid
            else:
                return arr[start] 
            mid = (start + end)//2
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.minNumber(A,0,N-1))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends