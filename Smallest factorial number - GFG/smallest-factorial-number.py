#User function Template for python3

class Solution:
    def getFactors(self, n):
        cnt = 0
        while n % 5 == 0:
            cnt += 1
            n = n // 5
        return cnt
    
    def totalfives(self, n):
        cnt = 0
        for i in range(n, 0, -1):
            cnt += self.getFactors(i)
        return cnt
    
    def zero_count(self,x):
        denome = 5
        zeros = 0
        while(x>=denome):
            zeros+=(x//denome)
            denome*=5
        return zeros
    
    def findNum(self, n : int):
        # Complete this function
        start = 0
        end = n * 5
        ans = 0
        while start <= end:
            mid = (start + end)//2
            if self.zero_count(mid) >= n:
                end = mid - 1
                ans = mid
            elif self.zero_count(mid) < n:
                start = mid + 1
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends