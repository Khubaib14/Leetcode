class Solution:
    def ConverttoAscii(self, letters):
        results = []
        for i in letters:
            results.append(ord(i))
        return results
    
    def BinarySearch(self, arr, target):
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end)//2
            if arr[mid] == target:
                return mid + 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start
    
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
        
        
        
        """
        result = self.ConverttoAscii(letters)
        ans = self.BinarySearch(result, ord(target))
        if ans >= len(letters):
            return letters[0]
        else:
            return letters[ans]
        """