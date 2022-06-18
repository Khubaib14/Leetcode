class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1
        return start