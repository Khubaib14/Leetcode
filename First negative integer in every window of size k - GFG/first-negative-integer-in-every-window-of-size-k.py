#User function Template for python3

def printFirstNegativeInteger(A, N, K):
   NegQueue = []
   result = []
   for i in range(K):
       if A[i] < 0:
           NegQueue.append(A[i])
   result.append(NegQueue[0] if len(NegQueue) > 0 else 0)
   
   for i in range(K,len(A)):
       if len(NegQueue) > 0 and A[i - K] == NegQueue[0]:
           NegQueue.pop(0)
       if A[i] < 0:
           NegQueue.append(A[i])
       result.append(NegQueue[0] if len(NegQueue) > 0 else 0)
   
   return result
    
    
    
    
    
def solOne(s, k):
    """
    This one hits TLE, otherwise works fine.
    """
    slow = 0
    fast = 0
    l = []
    
    while fast < len(s):
        if fast - slow + 1 < k:
            fast += 1
        elif fast - slow + 1 == k:
            i = slow
            while i <= fast:
                if s[i] < 0:
                    l.append(s[i])
                    break
                i += 1
            if i == fast+1:
                l.append(0)
            fast += 1
            slow += 1
    return (l)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends