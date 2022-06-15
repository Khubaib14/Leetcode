#User function Template for python3

class Solution:
	def BinarySearch(self, arr):
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end)//2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid]:
                start = mid + 1
            elif arr[mid - 1] > arr[mid]:
                end = mid - 1
	
	def findPeakElement(self, arr):
		# Code here
		if arr[-1] > arr[-2]:
            return arr[-1]
        elif len(arr) < 3 and arr[-1] < arr[-2]:
            return arr[-2]
        elif len(arr) >= 3:
            return arr[self.BinarySearch(arr)]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		a = list(map(int,input().split()))
		ob = Solution();
		ans = ob.findPeakElement(a)
		print(ans)




# } Driver Code Ends