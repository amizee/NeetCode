from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        cycle = set()
        cycleStart = -1

        def dfs(node, par):
            nonlocal cycleStart
            if node in visit:
                cycleStart = node
                return True

            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []

# Intuition: brute force approach is to build the graph one edge at a time and dfs through the graph to check for cycles. The first edge you add that causes a cycle is the redundant connection. (i.e. its the last cycle edge in the list)
# Optimal - only dfs() through the graph once. Use a set visit to check for cycles. Once you've found a cycle, this must be the node where the cycle begins, so you set cycleStart to this node.
# When the recursion returns back, mark every node as part of the path of the cycle until you reach cycleStart in a set.
# Now you have every node that is part of the cycle edges in "cycle"
# By looping through the edges in reverse order and checking both nodes exist in "cycle", it returns the correct edge.