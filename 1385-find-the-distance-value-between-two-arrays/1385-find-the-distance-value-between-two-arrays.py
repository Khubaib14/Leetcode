class Solution:
    def BinarySearch(self, arr, target, d):
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end)//2
            dist = abs(arr[mid] - target)
            if dist <= d:
                return False
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return True
    
    
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort() 
        cnt = 0
        for i in arr1:
            if self.BinarySearch(arr2, i, d):
                cnt += 1
        return cnt