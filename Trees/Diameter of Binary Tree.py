class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0

            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)

            self.res = max(self.res, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return self.res

# Intuition: very similar to "Balanced Binary Tree" - DFS to calculate the height of the left and right subtree and using a "global" res variable to store the max diameter.