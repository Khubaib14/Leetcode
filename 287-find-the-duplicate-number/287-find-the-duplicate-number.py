class Solution:
    def findDuplicate(self, s: List[int]) -> int:
        i = 0

        # swap sort processing
        # returns swap sorted string s
        while i < len(s):
            if s[i] != s[s[i] - 1]:
                s[s[i] - 1], s[i] = s[i], s[s[i] - 1]
            else:
                i += 1
        # observation on swap sorted s
        for i in range(len(s)):
            if s[i] != (i+1):
                return (s[i])
        
        
        
        
        
        
        
    def solOne(nums):    
        fast = 0
        d = {}
        while fast < len(nums):
            d[nums[fast]] = d.get(nums[fast], 0) + 1
            if d[nums[fast]] > 1:
                return nums[fast]
            fast += 1