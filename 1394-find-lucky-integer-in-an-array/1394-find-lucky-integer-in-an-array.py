class Solution:
    def findLucky(self, nums: List[int]) -> int:
        d, l = dict(), []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for key, value in d.items():
            if key == value:
                l.append(key)
        if len(l) > 0:
            return max(l)
        else:
            return -1