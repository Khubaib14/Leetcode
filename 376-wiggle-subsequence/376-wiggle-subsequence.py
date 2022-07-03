class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        flag = None
        total = 1

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i] and flag != True:
                total += 1
                flag = True
            elif nums[i-1] > nums[i] and flag != False:
                total += 1
                flag = False

        return total