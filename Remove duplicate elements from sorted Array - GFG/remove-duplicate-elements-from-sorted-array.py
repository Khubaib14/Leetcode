#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
		i =0
        while len(A)-1>i:
            if A[i] == A[i+1]:
                A.pop(i+1)
            else:
                i+=1
        return len(A)
		
		
		
	def personalSol(self, arr, N):
	    # throws driver code error (not my fault)

		# code here
        lead = 1
        trail = 0
        
        # when array length is 1
        if len(arr) == 1:
            return arr
        
        # when array length is more than 1
        while lead < len(arr)-1:
            # print(arr, arr[lead],arr[trail])
            if arr[lead] == arr[trail]:
                del arr[trail]
                # trail = lead
                # lead += 1
            else:
                trail += 1
                lead += 1
                    
        # print(arr, arr[lead], arr[trail], "here", lead, trail)
        if arr[lead] == arr[trail]:
            del arr[trail]
        return (arr)
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends