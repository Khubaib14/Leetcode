class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {} # d = {element:index}
    
        # create element-index map
        for i in range(len(nums)):
            d[nums[i]] = i

        # replace the elements/keys of the dict
        for i in range(len(operations)):
            d[operations[i][1]] = d.pop(operations[i][0])

        # based on index, recreate array    
        for i,j in d.items():
            nums[j] = i
        return nums