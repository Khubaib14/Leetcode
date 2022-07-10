class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
            if nums[slow] != 0:
                slow += 1
        
        
        
    def solOne(self, nums):
        pointer = 0
        result = []
        cnt = 0
        while pointer < len(nums):
            if nums[pointer] != 0:
                result.append(nums[pointer])
            else:
                cnt += 1
            pointer += 1
        result.extend([0]*cnt)
        return result