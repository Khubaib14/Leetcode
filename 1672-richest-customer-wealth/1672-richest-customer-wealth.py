class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max({i:[sum(accounts[i])] for i in range(len(accounts))}.values())[0]
        