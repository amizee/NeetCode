class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1

        return res

# Intuition: The only way that it's impossible is if the available gas is less than the cost to travel between the stations.
# e.g. if you start at -2 at the first station and the total gas is > total cost, it's guaranteed that at another station/s you'll gain back this +2 so a solution exists by just not starting at this station
# Loop through all the stations, if the gas goes below 0 then you can't start from this station so set res to the next station.