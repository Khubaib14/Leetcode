class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def sum_rec(x):
            if len(x) <= 1:
                return x[0]
            else:
                return x[0] + sum_rec(x[1:])
            
        def get_missing(nums):
            n = len(nums)
            return int((n*(n+1))//2 - sum_rec(nums))
        
        return get_missing(nums)