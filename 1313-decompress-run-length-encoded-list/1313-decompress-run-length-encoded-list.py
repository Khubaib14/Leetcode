class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(1, len(nums), 2):
            result += [nums[i]]*nums[i-1]
        return result
        
        
        
        
        
        
        
        
    def SolOne(self, nums):
        result = []
        times = 0
        
        for i in range(len(nums)):
            if i % 2 == 0: # i is even
                times = nums[i]
            else:
                for _ in range(times):
                    result.append(nums[i])

        return (result)