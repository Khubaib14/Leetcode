class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        maximum = 0
        total = 0

        while fast < len(nums):
            if nums[fast] == 1:
                fast += 1
                total += 1
            elif nums[fast] == 0:
                total = 0
                fast += 1
                slow = fast

            total = fast - slow
            maximum = max(maximum, total)
            
        return maximum
