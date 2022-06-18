class Solution:
    def isPerfectSquare(self, k: int) -> bool:
        start = 0
        end = k
        while start <= end:
            mid = (start + end)//2
            sq = mid * mid
            if sq == k:
                return True
            elif sq > k:
                end = mid - 1
            elif sq < k:
                start = mid + 1
        return False