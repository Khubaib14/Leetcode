class Solution:
    def maxPower(self, s: str) -> int:
        fast = 0
        curr = 0
        maximum = 0
        length = 0

        while fast < len(s):
            if ord(s[fast]) == curr:
                length += 1

            elif ord(s[fast]) != curr:
                curr = ord(s[fast])
                length = 0

            fast += 1
            maximum = max(length, maximum)

        return (maximum+1)
