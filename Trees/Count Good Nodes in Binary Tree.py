# My solution
class Solution:   
  def goodNodes(self, root: TreeNode) -> int:
          self.res = 0

          def dfs(curr, currMax):
              if not curr:
                  return 

              if curr.val >= currMax:
                  self.res += 1
              currMax = max(curr.val, currMax)
              dfs(curr.left, currMax)
              dfs(curr.right, currMax)

          dfs(root, root.val)
          return self.res

# Cleaner solution for tracking the result, handled within the DFS function by doing res += dfs() and returning 0 or 1
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def dfs(curr, currMax):
            if not curr:
                return 0
            
            res = 1 if curr.val >= currMax else 0
            currMax = max(curr.val, currMax)
            res += dfs(curr.left, currMax)
            res += dfs(curr.right, currMax)
            return res

        return dfs(root, root.val)
    
# Intuition: Along the path from the root to any node x, track the highest value before reaching x. This way, upon visiting each node a simple conditional checks if the node is a good node or not.
