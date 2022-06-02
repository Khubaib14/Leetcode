class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = 0
        for i in nums:
            if count == 0:
                element = i
            if element == i:
                count += 1
            else:
                count -= 1
        return element
        
        
    def Sort(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        
            
    def hashmap(self, nums):
        if len(nums) == 1:
            return nums[0]
        mark = len(nums)//2
        d = {}
        for i in nums:
            if i in d:
                if d[i] >= mark:
                    return i
            d[i] = d.get(i, 0) + 1