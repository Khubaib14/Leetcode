class Solution:
    def GetMaxDiff(self, arr, h):
        # h is with horizontalCuts
        i = 0
        arr.extend([0,h])
        arr.sort(reverse = True)
        maxdiff = 0
        cut1 = 0
        cut2 = 0
        for i in range(1, len(arr)):
            if (arr[i-1] - arr[i]) > maxdiff:
                maxdiff = (arr[i-1] - arr[i])
                cnt1 = i-1
                cnt2 = i
        return (cnt1, cnt2, maxdiff)
    
    
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        htuple = self.GetMaxDiff(horizontalCuts, h)
        vtuple = self.GetMaxDiff(verticalCuts, w)
        return (htuple[2]*vtuple[2])%(10**9+7)