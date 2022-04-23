class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        slow = 0
        fast = 0
        l = []
        windowsize = 3
        result = 0

        while fast < len(s):
            l.append(s[fast])
            if fast - slow + 1 < windowsize:
                fast += 1
            elif fast - slow + 1 == windowsize:
                if len(set(l)) == 3:
                    result += 1
                if s[slow] == l[0]:
                    l.pop(0)
                slow += 1
                fast += 1

        return result
