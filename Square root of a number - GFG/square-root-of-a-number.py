#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, n): 
    #Your code here
        start = 0
        end = n
        ans = 0
        while start <= end:
            mid = (start + end)//2
            # print(start, end, mid)
            if mid * mid > n:
                end = mid - 1
            elif mid * mid <= n:
                ans = mid 
                start = mid + 1
        return ans
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends