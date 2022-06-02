#User function Template for python3

def chocolates (arr, n) : 
    #Complete the function
    start = 0
    end = len(arr) - 1
    
    while start < end and len(arr) > 1:
        if arr[start] > arr[end]:
            start += 1
        elif arr[start] < arr[end]:
            end -= 1
        else:
            end -= 1
        
    
    return (arr[start])


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = chocolates(arr, n)
    print(ans)
    





# } Driver Code Ends