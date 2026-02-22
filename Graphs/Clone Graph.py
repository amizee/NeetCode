"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        adjList = {}
        
        def dfs(node):
            if node in adjList:
                return

            newNode = Node(node.val)
            adjList[node] = newNode
            for neighbor in node.neighbors:
                dfs(neighbor)
                newNode.neighbors.append(adjList[neighbor])

        dfs(node)
        return adjList[node]

# Intuition: graph is represented as an adjacency list. Similar to another cloning problem, store cloned nodes in a hashmap (using the old node as the key) so that it can be obtained globally in O(1) time
# As it's an object reference when you update it, it gets updated in all the other nodes too.
# Run dfs to clone each node, first checking if it's already been cloned using the adjList. Otherwise, we simply add the neighbour using its key-value pair from the hashmap.