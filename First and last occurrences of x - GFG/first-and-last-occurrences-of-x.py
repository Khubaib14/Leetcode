#User function Template for python3


def find(arr,n,x):
    # code here
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