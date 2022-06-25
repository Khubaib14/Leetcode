class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = 100000000
        mx = 0
        for i in nums:
            if i < mn:
                mn = i
            if i > mx:
                mx = i
        for i in range(mx, 0, -1):
            if mx%i == 0 and mn%i == 0:
                return i