class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        q = list(s)
        i = 0
        j = len(q) - 1
        while i < j:
            if not q[i].isalpha():
                i += 1
            elif not q[j].isalpha():
                j -= 1
            else:
                q[i], q[j] = q[j], q[i]
                i += 1
                j -= 1

        return "".join(q)