class Solution:
    def SearchLeft(self, arr, key):
        start = 0
        end = len(arr) - 1
        mid = (start+end)//2
        result = []
        while start <= end:
            if arr[mid] == key:
                result.append(mid)
                end = mid - 1
            elif arr[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end)//2
        return result
    
    
    def SearchRight(self, arr, key):
        start = 0
        end = len(arr) - 1
        mid = (start+end)//2
        result = []
        while start <= end:
            if arr[mid] == key:
                result.append(mid)
                start = mid + 1
            elif arr[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end)//2
        return result
    
    
    
    def targetIndices(self, arr: List[int], key: int) -> List[int]:
        lt_count, eq_count = 0, 0
        for n in arr:
            if n < key:
                lt_count += 1
            elif n == key:
                eq_count += 1
            
        return list(range(lt_count, lt_count+eq_count))
        
        
        
        
        #arr.sort()
        #l = list(set(self.SearchRight(arr, key) + self.SearchLeft(arr, key)))
        #l.sort()
        #return l