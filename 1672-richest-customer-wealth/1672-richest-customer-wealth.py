class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        hash_map = dict()
        for i in range(len(accounts)):
            hash_map[i] = sum(accounts[i])
        return max(hash_map.values())
        