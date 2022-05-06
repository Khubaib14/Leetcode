class Solution:
    def sortedSquares(self, s: List[int]) -> List[int]:
        slow = 0
        fast  = len(s) - 1

        while slow <= fast:
            if abs(s[slow]) > abs(s[fast]):
                temp = s.pop(slow)
                s.insert(fast, temp)
            else:
                fast -= 1
                
        return [s[i]**2 for i in range(len(s))]