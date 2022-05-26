#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    #data structure to store sum of subsets
	    lis = []
	    #helper function call
	    self.helper(arr,0,0,N,lis)
	    #returning the list with sum of all subsets
	    return lis
	    
	    #p is pointer of index to be increased from 0 to n
	    #s is sum, we will either include the current index in sum or exclude
	    #ans is list data structure to store final solution
	def helper(self,arr,p,s,N,ans):
	    #if pointer reaches N, we have to lock in the sum in list and return
	    if p==N:
	        ans.append(s)
	        return
	    #at every index pointer we either decide the include that value in sum or exclude giving us all ways in which subsets can be formed
	    self.helper(arr,p+1,s+arr[p],N,ans)
	    self.helper(arr,p+1,s,N,ans)
	
	
	# below is my personal code which work perfectly fine
	# except that it returns the sum in some other ordering ¯\_(ツ)_/¯ 
	def Solve(self, ip, op=0, l= []):
        if len(ip) == 0:
            print(op)
            return 
        op1 = op
        op2 = op
        
        op2 += ip[0]
        ip = ip[1:]
        
        self.Solve(ip, op1)
        self.Solve(ip, op2)
        
        return
	
	def personal_subsetSums(self, arr, N):
		# code here
		l = []
    
        self.Solve(arr, 0, l)
        
        return l
    		 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends