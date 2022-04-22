class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0


        for i in words:
            for j in i:
                if j in allowed:
                    pass
                else:
                    count -= 1
                    break
            count += 1
        
        return count