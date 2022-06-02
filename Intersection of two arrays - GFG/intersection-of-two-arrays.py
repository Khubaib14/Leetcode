#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        
        #code here
        if len(b) < len(a):
            lower = b
            upper = a
        else:
            lower = a
            upper = b
            
        d = {}
        
        for i in lower:
            d[i] = d.get(i, 0) + 1
        
        count = 0
        upper = set(upper)
        for i in upper:
            if i in d:
                count += 1
        return (count)
        
        
    def solOne(self, a, b, n, m):
        if len(b) < len(a):
            lower = b
            upper = a
        else:
            lower = a
            upper = b
            
        d = {}
        
        for i in lower:
            d[i] = d.get(i, 0) + 1
        
        count = 0
        upper = set(upper)
        for i in upper:
            if i in d:
                count += 1
        return (count)
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob = Solution()
        
        print(ob.NumberofElementsInIntersection(a,b,n,m))
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
                
# } Driver Code Ends