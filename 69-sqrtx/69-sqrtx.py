class Solution:
    def mySqrt(self, k: int) -> int:
        start = 0
        end = k
        mid = (start + end)//2
        ans = -1
        while start <= end:
            square = mid * mid
            if square == k:
                return mid
            elif square < k:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end)//2
        return ans