#User function Template for python3
# Sone fuck-all error in line 58 leads to TCs failing.

class Solution:
    
    """def NearestGreaterLeftIndex(self, arr):
        result = []
        stk = []
        for i in range(len(arr)):
            if not stk:
                result.append(-1)
            elif stk[-1][0] > arr[i]:
                result.append(stk[-1][1])
            elif stk[-1][0] < arr[i]:
                while stk and stk[-1][0] < arr[i]:
                    stk.pop()
                if not stk:
                    result.append(-1)
                else:
                    result.append(stk[-1][1])
            stk.append((arr[i], i))
        return result"""
    
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,arr,n):
        #code here
        """temp = self.NearestGreaterLeftIndex(arr)
        return [i-temp[i] for i in range(len(temp))]"""
        stack = []
        ans=[]
        for i in range(n):
            if len(stack) == 0:
                ans.append(-1)
            elif len(stack)>0:
                while len(stack)>0 and stack[-1][0]<=arr[i]:
                    stack.pop()
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack[-1][1])
            stack.append([arr[i],i])
        
        for i in range(n):
            ans[i] = i-ans[i]
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nikhil Kumar Singh

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj = Solution()
        ans = obj.calculateSpan(a, n);
        for i in range(n):
            print(ans[i],end=" ")
        print()            
# } Driver Code Ends