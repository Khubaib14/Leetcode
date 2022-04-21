class Solution:
    def sortSentence(self, s: str) -> str:
        result = [0]*len(s.split(" "))
        fast = 0
        slow = 0
        length = 0

        while fast < len(s):
            if s[fast].isnumeric():
                result[int(s[fast])-1] = s[slow:fast]
                if fast < len(s):
                    fast += 2
                    slow = fast
            else:
                fast += 1

        return " ".join(result)
        