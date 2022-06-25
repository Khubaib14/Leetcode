class Solution:
    def BS(self, arr, target):
        start = 0
        end = len(arr) - 1
        ans = -1
        while start <= end:
            mid = (start + end)//2
            if arr[mid] < target:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans
    
    
    def specialArray(self, arr: List[int]) -> int:
        arr.sort()
        for i in range(1, max(arr)+1):
            calc = len(arr) - (self.BS(arr, i) + 1)
            if calc == i:
                return i
        return -1