class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1

        mid = (start + end)//2

        while start <= end:
            print(mid, arr[mid])
            if arr[mid+1] < arr[mid] and arr[mid-1] < arr[mid]:
                return mid
            elif arr[mid] < arr[mid+1]:
                start = mid 
            elif arr[mid-1] > arr[mid]:
                end = mid 

            mid = (start + end)//2

        return -1
        
        
        
        
        
    def solOne(self, arr):
        start = 0
        end = len(arr) - 1

        mid = (start + end)//2

        while start <= end:
            print(mid, arr[mid])
            if arr[mid+1] < arr[mid] and arr[mid-1] < arr[mid]:
                return mid
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                start = mid 
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                end = mid 

            mid = (start + end)//2

        return -1