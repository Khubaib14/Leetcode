class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # break into two
        lst1 = nums[:n]
        lst2 = nums[n:]

        # make new empty list
        nums = []

        # run a loop, taking same index from each
        for i in range(n):
            nums.append(lst1[i])
            nums.append(lst2[i])

        return nums