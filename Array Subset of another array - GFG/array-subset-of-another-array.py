#User function Template for python3

def BinarySearch(arr, k): # arr = a1
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


def isSubset( a1, a2, n, m):
    a1.sort()
    for i in a2:
        if not BinarySearch(a1, i):
            return "No"
    return "Yes"

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends