class Solution:
    def sortedSquares(self, s: List[int]) -> List[int]:
        
        result = [0]*len(s)

        slow = 0
        fast  = len(s) - 1
        append_pointer = len(s) - 1

        for i in range(len(s)):
            slow_square = s[slow]**2
            fast_square = s[fast]**2
            if slow_square >= fast_square:
                result[append_pointer] = slow_square
                slow += 1
            else:
                result[append_pointer] = fast_square
                fast -= 1
            append_pointer -= 1
        
        return (result)
        
        
        
    def solTwo(self, s: List[int]) -> List[int]:
        result = []

        slow = 0
        fast  = len(s) - 1

        for i in range(len(s)):
            slow_square = s[slow]**2
            fast_square = s[fast]**2
            if slow_square >= fast_square:
                result.insert(0,slow_square)
                slow += 1
            else:
                result.insert(0,fast_square)
                fast -= 1
        
        return (result)
        

        
    def solOne(self, s: List[int]) -> List[int]:
        slow = 0
        fast  = len(s) - 1

        while slow <= fast:
            if abs(s[slow]) > abs(s[fast]):
                temp = s.pop(slow)
                s.insert(fast, temp)
            else:
                fast -= 1
                
        return [s[i]**2 for i in range(len(s))]