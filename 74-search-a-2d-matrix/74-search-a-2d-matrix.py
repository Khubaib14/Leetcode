class Solution:
    def BinarySearchFloor(self, arr, target):
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            tolook = matrix[i][len(matrix[i])-1]
            if tolook == target:
                return True
            elif self.BinarySearchFloor(matrix[i], target) != -1:
                return True
        return False