class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = -1
        max2 = -1
        index = 0

        for i in range(len(nums)):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
            elif nums[i] > max2:
                max2 = nums[i]

        if max1 >= max2*2:
            return nums.index(max1)
        else:
            return -1    
        
        
    def solOne(nums):
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