class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)
            for neighbour in adj[node]:
                if neighbour == parent:
                  continue
                if not dfs(neighbour, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n

# Intuition: a graph is a valid tree if it doesn't contain a cycle and it's fully connected. A tree with n nodes can have at most n-1 edges otherwise it contains a cycle (i.e. each node has can only be reached by one path)
# If a graph is valid, you can dfs() from any node in the tree to check.
# This dfs takes in the node and parent to prevent false cycle detection, since its an undirected graph the edge is essentially stored twice in the adjacency list, so this prevents a cycle where you go back to the parent using the same edge.
# Use a set or an array - [False * (n + 1)] to store visited nodes so far.