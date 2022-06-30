#User function Template for python3

def deleteElement (arr, n, k) : 
    #Complete the function
    stk = []
    for i in arr:
        while stk and stk[-1] < i and k > 0:
            stk.pop()
            k -= 1
        stk.append(i)
    return stk


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = deleteElement(arr, n, k)
    print(*ans)
# } Driver Code Ends