class Solution:
    def minCostClimbingStairs(self, stairs: List[int]) -> int:
        costs = {-1: 0, 0: 0}
        top = len(stairs) + 1
        for stair, cost in enumerate(stairs, 1):
            one_step = costs[stair - 1] + cost
            two_steps = costs[stair - 2] + cost
            costs[stair] = min(one_step, two_steps)
        
        return min(costs[top - 1], costs[top - 2])