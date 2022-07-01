class Solution:
    def FreqArr(self, arr):
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        return d
    
    
    def print_next_greater_freq(self,arr,n):
        # code here
        d = self.FreqArr(arr)
        stk = []
        result = []
        for i in range(len(arr)-1, -1, -1):
            if len(stk) == 0:
                result.append(-1)
            elif d[stk[-1]] > d[arr[i]]:
                result.append(stk[-1])
            elif d[stk[-1]] <= d[arr[i]]:
                while stk and d[stk[-1]] <= d[arr[i]]:
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
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        obj=Solution()
        ans=obj.print_next_greater_freq(arr,n)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends