class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        limit = 1
        maxer = 0

        while fast < len(nums):
            if nums[fast] == 0:
                limit -= 1

            if limit < 0:
                while limit < 0:
                    if nums[slow] == 0:
                        limit += 1
                    slow += 1

            fast += 1 
            maxer = max((fast-slow-1), maxer)    
            # print(nums[slow:fast+1], maxer, limit)

        return (maxer)