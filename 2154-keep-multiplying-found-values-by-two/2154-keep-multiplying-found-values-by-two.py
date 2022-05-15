class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            for i in nums:
                if original == i:
                    original *= 2
                    break

        return (original)
        
        
        
        
        
        
        
        
        
    def solOne(nums):
        d = {}

        for i in nums:
            d[i] = d.get(i,0) + 1


        while original in d:
            original = original * 2

        return (original)

    