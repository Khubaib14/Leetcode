#User function Template for python3

def BinarySearch(arr, k):
    start = 0
    end = len(arr) - 1

    mid = (start + end)//2
    
    while start <= end:
        if arr[mid] == k:
            return True
        elif arr[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end)//2
    
    return False


def check (arr,  brr, n) : 
    #Complete the function
    s1=set(arr)
    s2=set(brr)
    for i in s1:
       if arr.count(i)!=brr.count(i):
           return 0
    return 1


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    brr = list(map(int,input().strip().split()))
    
    print(check(arr, brr, n))




# } Driver Code Ends