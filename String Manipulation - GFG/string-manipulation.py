
class Solution:
    def removeAdj(self,arr,n):
        # Your code goes here
        stk = []
        for i in arr:
            if stk and stk[-1] == i:
                stk.pop()
            else:
                stk.append(i)
        return len(stk)
        
    

#{ 
#  Driver Code Starts

if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        v=[x for x in input().split()]
        ob = Solution()
        print(ob.removeAdj(v,n))
# } Driver Code Ends