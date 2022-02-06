class Solution:
    def findLucky(self, nums: List[int]) -> int:
        d, l = dict(), []
        for i in set(nums):
            d[i] = 0
        for i in nums:
            d[i] += 1
        for key, value in d.items():
            if key == value:
                l.append(key)
        if len(l) > 0:
            return max(l)
        else:
            return -1