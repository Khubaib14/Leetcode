class Solution:
    def BinarySearch(self, arr, target, starter):
        start = starter
        end = len(arr) - 1
        ans = -1
        while start <= end:
            mid = (start + end)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                start = mid + 1
            else:
                end = mid - 1

        if end < starter:
            return -1
        else:
            return end
    
    def BinarySearchBased(self, numsi, numsj):
        diff = -1
        for i in range(len(numsi)):
            end = self.BinarySearch(numsj, numsi[i], i)
            if end == -1:
                diff = max(diff, 0)
            else:
                diff = max(diff, (end-i))
        return diff
    
    def maxDistance(self, numsi: List[int], numsj: List[int]) -> int:
        diff = 0
        i = 0
        j = 0
        while i < len(numsi) and j < len(numsj):
            if numsi[i] <= numsj[j]:
                diff = max(diff, j-i)
                j += 1
            else:
                i += 1
                j += 1
        return diff

    