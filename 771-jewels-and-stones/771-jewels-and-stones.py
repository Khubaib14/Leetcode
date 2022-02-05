class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        count = 0
        for i in list(stones):
            if i in jewels:
                count = count + 1
        return count