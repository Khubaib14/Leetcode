class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 0
        end = n
        ans = -1
        while start <= end:
            mid = (start + end)//2
            formula = ((mid+1)*mid)//2
            if formula <= n:
                ans = mid
                start = mid + 1 
            else:
                end = mid - 1
        return ans