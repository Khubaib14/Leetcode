class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1]*len(nums1)
        push = 0
        for i in nums1:
            cnt = 0
            for j in nums2:
                if j == i:
                    for k in nums2[cnt:]:
                        if k > j:
                            result[push] = k
                            break
                    push += 1
                else:
                    cnt += 1

        return result