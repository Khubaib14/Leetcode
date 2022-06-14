class Solution:
    def SearchRight(self, arr, key):
        start = 0
        end = len(arr) - 1
        mid = (start+end)//2
        ans = -1
        while start <= end:
            if arr[mid] == key:
                ans = mid
                start = mid + 1
            elif arr[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end)//2
        return ans
    
    def SearchLeft(self, arr, key):
        start = 0
        end = len(arr) - 1
        mid = (start+end)//2
        ans = -1
        while start <= end:
            if arr[mid] == key:
                ans = mid
                end = mid - 1
            elif arr[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end)//2
        return ans
    
    
    def searchRange(self, arr: List[int], key: int) -> List[int]:
        arr.sort()
        right = self.SearchRight(arr, key) 
        left = self.SearchLeft(arr, key)
        #print(SearchRight(arr, key), "Right")
        #print(SearchLeft(arr, key), "Left")
        if right == -1 or left == -1:
            return [-1, -1]
        return [left, right]