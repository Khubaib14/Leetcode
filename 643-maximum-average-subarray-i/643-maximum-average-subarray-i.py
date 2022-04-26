class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        slow = 0
        fast = 0
        total = 0
        greatest_avg = -1000000 # based on constraints provided

        while fast < len(nums):
            total += nums[fast]

            if fast - slow + 1 < k:
                fast += 1

            elif fast - slow + 1 == k:
                if (total/k) > greatest_avg:
                    greatest_avg = total/k
                total -= nums[slow]
                fast += 1
                slow += 1
        
        return greatest_avg
