class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            s = sum(nums[0:i+1])
            ans[i] = s
        return ans