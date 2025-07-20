class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        tot_cost = 0
        cost_diff = []

        for cost in costs:
            tot_cost += cost[0]
            cost_diff.append(cost[1] - cost[0])
        
        cost_diff.sort()
        for i in range(len(costs) // 2):
            tot_cost += cost_diff[i]

        return tot_cost
