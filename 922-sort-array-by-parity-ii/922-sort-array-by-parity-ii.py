class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = 1
        even = 0

        while odd < len(nums) and even < len(nums):
            if nums[odd] % 2 == 1:
                odd += 2
            elif nums[even] % 2 == 0:
                even += 2
            else: 
                nums[odd], nums[even] = nums[even], nums[odd]
                even += 2
                odd += 2
        return (nums)
        
        
    def solOne(nums):
        odd = 1
        even = 0
        size = len(nums)
        while odd < size and even < size:
            if (nums[odd] % 2 == 0) and (nums[even] % 2 != 0):
                nums[odd], nums[even] = nums[even], nums[odd]
                odd += 2
                even += 2
            elif (nums[odd] % 2 == 0) and (nums[even] % 2 == 0):
                even += 2
            elif (nums[odd] % 2 != 0) and (nums[even] % 2 != 0):
                odd  += 2
            elif (nums[odd] % 2 != 0) and (nums[even] % 2 == 0):
                odd += 2
                even += 2

        return (nums)