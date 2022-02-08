class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            for j in nums:
                if i == j:
                    count += 1
        return (count - len(nums))//2
        