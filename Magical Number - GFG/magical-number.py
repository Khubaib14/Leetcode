#User function Template for python3

def binarySearch(arr,low,high):
    '''
    arr: given array
    low: low index initialize as zero
    high: high index initialize as len(arr)-1
    return: magical n.o or -1
    '''
    while low <= high:
       
        mid = low +(high-low)//2 #find mid index
       
        if mid == arr[mid]:
            return mid
       
        elif mid < arr[mid]:
            high = mid - 1
       
        else:
            low = mid + 1
   
    return -1


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        print(binarySearch(arr,0,n-1))
# } Driver Code Ends