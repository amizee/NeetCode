from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            if visit[node]:
                return
            
            visit[node] = True
            for neigbour in adj[node]:
                dfs(neigbour)
        
        res = 0
        for i in range(n):
            if not visit[i]:
                dfs(i)
                res += 1
        return res
    