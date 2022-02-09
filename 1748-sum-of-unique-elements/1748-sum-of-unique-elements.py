class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        empty_dic = dict()
        for i in nums:
            if i in empty_dic:
                empty_dic[i] += 1
            else:
                empty_dic[i] = 1

        return sum([k for k,v in empty_dic.items() if v == 1])
        