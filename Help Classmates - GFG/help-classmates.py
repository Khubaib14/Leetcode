#User function Template for python3

class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        stk = []
        result = []
        for i in range(len(arr)-1, -1, -1):
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
        result.reverse()
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [ int(x) for x in input().split() ]
        obj = Solution()
        result = obj.help_classmate(arr,n)
        for i in result:
            print(i,end=' ')
        print()

# } Driver Code Ends