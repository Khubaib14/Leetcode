#User function Template for python3

def longestSubarry( arr, N):
    slow = 0
    fast = 0
    maxer = 0
    
    while fast < len(arr):
        # maxer = max(maxer, (fast-slow+1))
        # print(arr[slow:fast+1], 'top')
        if arr[fast] < 0:
            maxer = max(maxer, (fast-slow))
            # print(arr[slow:fast+1], 'middle')
            slow = fast+1
        maxer = max(maxer, (fast-slow+1))
         #print(arr[slow:fast+1], 'bottom')
        fast += 1
            
    return (maxer) 
    
    
    
def solOne(arr,N):
    slow = 0
    fast = 0
    l = []
    maxer = 0
    
    while fast < len(arr):
        l.append(arr[fast])
        # maxer = max(len(l), maxer)
        if l and l[-1] < 0:
           while l and l[-1] < 0:
               del l[0]
               slow += 1
        maxer = max(len(l), maxer)
        fast += 1
        
    return (maxer)
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(longestSubarry(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends