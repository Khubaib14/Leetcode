class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # I managed to solve this question by BS!
        # However, the sorting process in order to return ans in 
        # increasing order led to TLE.
        # Hence had to do this...
        return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]