class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxindex = 0
        maxelement = 0
        secondmax = 0

        for i in range(len(nums)):
            if nums[i] > maxelement:
                maxelement = nums[i]
                maxindex = i

        for i in nums:
            if i > secondmax and i != maxelement:
                secondmax = i

        if maxelement >= secondmax * 2:
            return maxindex
        else:
            return -1