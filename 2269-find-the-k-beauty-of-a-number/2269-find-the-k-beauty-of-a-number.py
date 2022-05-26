class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numstr = str(num)
        slow = 0
        fast = 0
        count = 0

        while fast < len(numstr):
            if fast - slow + 1 < k:
                fast += 1
            else:
                numpart = int(numstr[slow:fast+1])
                if numpart == 0:
                    pass
                elif num % numpart == 0:
                    count += 1
                else:
                    pass
                slow += 1
                fast += 1


        return (count)