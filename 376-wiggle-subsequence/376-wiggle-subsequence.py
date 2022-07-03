class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        rise = None
        total = 1

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i] and rise != True:
                total += 1
                rise = True
            elif nums[i-1] > nums[i] and rise != False:
                total += 1
                rise = False

        return total