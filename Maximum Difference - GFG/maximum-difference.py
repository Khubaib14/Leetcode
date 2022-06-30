class Solution:
    # Your task is to complete this function
    # Function should return an integer denoting the required answer
    def NSR(self, arr):
        stk = []
        result = []
        for i in range(len(arr)-1, -1, -1):
            if len(stk) == 0:
                result.append(0)
            elif stk[-1] < arr[i]:
                result.append(stk[-1])
            elif stk[-1] >= arr[i]:
                while stk and stk[-1] >= arr[i]:
                    stk.pop()
                if not stk:
                    result.append(0)
                else:
                    result.append(stk[-1])
            stk.append(arr[i])
        result.reverse()
        return result
            
    def NSL(self, arr):
        stk = []
        result = []
        for i in range(len(arr)):
            if len(stk) == 0:
                result.append(0)
            elif stk[-1] < arr[i]:
                result.append(stk[-1])
            elif stk[-1] >= arr[i]:
                while stk and stk[-1] >= arr[i]:
                    stk.pop()
                if not stk:
                    result.append(0)
                else:
                    result.append(stk[-1])
            stk.append(arr[i])
        return result
        
    def findMaxDiff(self, arr, n):
        # Code here
        nsl = self.NSL(arr)
        nsr = self.NSR(arr)
        result = []
        for i,j in zip(nsl, nsr):
            result.append(abs(i-j))
        return max(result)

#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.findMaxDiff(arr, n))
#Contributed By: Harshit Sidhwa
# } Driver Code Ends