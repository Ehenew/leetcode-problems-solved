class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:       
        tot_tank = 0
        s_index = 0
        
        curr_gas = 0

        for i in range(len(gas)):

            curr_gas += gas[i] - cost[i]
            # tot_tank += curr_gas # ??? \U0001f622
            tot_tank += gas[i] - cost[i]

            if curr_gas < 0:
                s_index = i + 1
                curr_gas = 0                

        if tot_tank >=0:
            return s_index
        else:
            return - 1


