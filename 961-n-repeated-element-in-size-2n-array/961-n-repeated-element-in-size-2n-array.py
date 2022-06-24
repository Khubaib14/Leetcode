class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        half = len(nums)//2
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] == half:
                return i