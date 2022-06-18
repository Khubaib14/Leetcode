# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        ans = -1
        while start <= end:
            mid = (start + end)//2
            result = isBadVersion(mid)
            if not result:
                #ans = mid
                start = mid + 1
            elif result:
                ans = mid
                end = mid - 1
        return ans