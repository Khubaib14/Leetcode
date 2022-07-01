#User function Template for python3

def save_gotham (arr, n) : 
    #Complete the function
    stk = []
    result = []
    for i in range(len(arr)-1, -1, -1):
        if not stk:
            result.append(0)
        elif stk[-1] > arr[i]:
            result.append(stk[-1])
        elif stk[-1] <= arr[i]:
            while stk and stk[-1] <= arr[i]:
                stk.pop()
            if not stk:
                result.append(0)
            else:
                result.append(stk[-1])
        stk.append(arr[i])
    return sum(result)%1000000001


#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = save_gotham(arr, n)
    print(ans)
    





# } Driver Code Ends