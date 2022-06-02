class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mark = len(nums)//2
        d = {}
        for i in nums:
            if i in d:
                if d[i] >= mark:
                    return i
            d[i] = d.get(i, 0) + 1