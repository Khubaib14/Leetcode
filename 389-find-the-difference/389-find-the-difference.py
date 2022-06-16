class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        return chr(sum(list(map(ord, list(t)))) - sum(list(map(ord, list(s)))))