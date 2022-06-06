#User function Template for python3

def BinarySearchFirst(arr, k):
    start = 0
    end = len(arr) - 1
    mid = (start + end)//2
    
    first = -1
    
    while start <=  end:
        if arr[mid] == k:
            first = mid
            end = mid - 1
            
        elif arr[mid] < k:
            start = mid + 1
        else:
            end = mid - 1 
        
        mid = (start + end)//2
    
    return first
    

def BinarySearchLast(arr, k):
    start = 0
    end = len(arr) - 1
    mid = (start + end)//2
    
    last = -1
    
    while start <=  end:
        if arr[mid] == k:
            last = mid
            start = mid + 1
            
        elif arr[mid] < k:
            start = mid + 1
        else:
            end = mid - 1 
        
        mid = (start + end)//2
    
    return last


def find(arr,n,x):
    # code here
    first = BinarySearchFirst(arr, x)
    last = BinarySearchLast(arr, x)
    return first, last
    
    
    
    
    

#######################    
def solOne(arr,n,x):    
    a = []
    for i in range(n):
       if arr[i]==x:
           a.append(i)
    if len(a)==1:
       return a*2
    elif len(a)>1:
       return a[0],a[-1]
    else:
       return [-1,-1]

#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends