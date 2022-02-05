class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        final = [0]*(len(s))
        for i, j in zip(s, indices):
            final[j] = i
        return "".join(final)