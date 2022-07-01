# User function Template for Python3

class Solution:
    def leftSmaller(self, n, arr):
        # code here
        stk = []
        result = []
        for i in range(len(arr)):
            if len(stk) == 0:
                result.append(-1)
            elif stk[-1] < arr[i]:
                result.append(stk[-1])
            elif stk[-1] >= arr[i]:
                while stk and stk[-1] >= arr[i]:
                    stk.pop()
                if len(stk) == 0:
                    result.append(-1)
                else:
                    result.append(stk[-1])
            stk.append(arr[i])
        return result

#{ 
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
# } Driver Code Ends