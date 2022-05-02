class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        d = {}
        while fast < len(nums):
            d[nums[fast]] = d.get(nums[fast], 0) + 1
            if d[nums[fast]] > 1:
                return nums[fast]
            fast += 1