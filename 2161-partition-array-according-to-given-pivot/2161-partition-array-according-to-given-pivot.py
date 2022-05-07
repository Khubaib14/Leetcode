class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser = []
        greater = []

        for i in nums:
            if i < pivot:
                lesser.append(i)
            elif i > pivot:
                greater.append(i)

        result = lesser + [pivot]*(len(nums) - (len(lesser) + len(greater))) + greater
        
        return (result)
        
        
        
        
    def solOne(self, nums: List[int], pivot: int) -> List[int]:    
        result = [pivot]
        pivot_index_right = 0
        pivot_index_left = 0
        once_done = False

        for i in range(len(nums)):
            if nums[i] < pivot:
                result.insert(pivot_index_left, nums[i])
                pivot_index_left += 1
                pivot_index_right += 1
            elif nums[i] > pivot:
                result.append(nums[i])
            elif not once_done:
                once_done = True
            elif once_done and nums[i] == pivot:
                result.insert(pivot_index_left+1, nums[i])
                pivot_index_right += 1

        return (result)