class Solution:
    
    # for some fuck-all reason, the code does not work here,
    # the very same code which was working on the interpreter  ¯\_(ツ)_/¯
    # I have commented my own code below
    """
    def Solve(self, arr1, arr2, mix):
        if len(arr1) == 1 and len(arr2) == 1:
            mix.append(arr2[0])
            mix.append(arr1[0])
            return 
        else:
            last1 = arr1[-1]
            last2 = arr2[-1]
            arr1 = arr1[:len(arr1)-1]
            arr2 = arr2[:len(arr2)-1]
            
            self.Solve(arr1, arr2, mix)
            
            mix.append(last2)
            mix.append(last1)
            
        return mix
    
    def shuffleArray(self, arr, n):
        # Your code goes here
        arr1 = arr[len(arr)//2:]
        arr2 = arr[:len(arr)//2]
        mix = []
        self.Solve(arr1, arr2, mix)
        return mix
    """
    
    def shuffleArray(self, arr, n):
        arr1 = arr[:(n//2)]
        arr2= arr[(n//2):]
        
        for i in range(n):
            if i%2==0:
                arr[i]=arr1.pop(0)
                
            elif i%2==1:
                arr[i]=arr2.pop(0)
        arr.append('')        
        return arr

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends