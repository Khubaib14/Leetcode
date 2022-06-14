class Solution:
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
    
    
    
    def targetIndices(self, arr: List[int], key: int) -> List[int]:
        arr.sort()
        right = self.SearchRight(arr, key) 
        left = self.SearchLeft(arr, key)
        if right == -1 or left == -1:
            return []
        return [i for i in range(left, right+1)]
        
        
        
    def SolTwo(self, arr, key):
        lt_count, eq_count = 0, 0
        for n in arr:
            if n < key:
                lt_count += 1
            elif n == key:
                eq_count += 1
            
        return list(range(lt_count, lt_count+eq_count))