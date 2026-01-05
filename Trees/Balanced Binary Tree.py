class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.res = True
        def dfs(curr):
            if not curr:
                return 0
            
            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)

            if abs(leftHeight - rightHeight) > 1:
                self.res = False
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return self.res

# Intuition: This DFS calculates the height of the current node by taking 1 + the max of the left and right subtree and uses a conditional to check whether the tree is balanced.
# Similar solution to calculating the maximum depth of a binary tree