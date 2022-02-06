class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        nums1, nums2 = set(nums1), set(nums2)
        for i in nums1:
            if i in nums2:
                s.add(i)
        return s