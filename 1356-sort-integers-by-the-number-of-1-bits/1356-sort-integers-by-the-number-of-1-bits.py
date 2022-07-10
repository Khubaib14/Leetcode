class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda num : (sum((num >> i) & 1 for i in range(32)), num))
        
        
        
        
    def solOne(arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))