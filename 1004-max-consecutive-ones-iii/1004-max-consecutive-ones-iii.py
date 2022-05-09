class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        slow = 0
        fast = 0
        tolerance = k
        maximum = 0
        count = 0

        while fast <  len(nums):
            if nums[fast] == 1 and tolerance >= 0:
                fast += 1
            elif nums[fast] == 0 and tolerance >= 0:
                fast += 1
                tolerance -= 1

            if tolerance < 0:
                while tolerance < 0:
                    if nums[slow] == 1:
                        slow += 1
                    elif nums[slow] == 0:
                        tolerance += 1
                        slow += 1

            count = fast - slow + 1
            maximum = max(maximum, count)
            # print(nums[slow:fast+1], count, tolerance)

        return (maximum-1)