class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        point = 0
        pay = 0
        while point < len(cost):
            if (point+1) % 3 != 0 or point == 0:
                pay += cost[point]
            point += 1
        return pay    