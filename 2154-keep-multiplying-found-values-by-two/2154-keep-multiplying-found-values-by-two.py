class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        d = {}

        for i in nums:
            d[i] = d.get(i,0) + 1


        while original in d:
            original = original * 2

        return (original)

    