class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(curr, minVal, maxVal):
            if not curr:
                return True
            
            if not (minVal < curr.val < maxVal):
                return False

            return dfs(curr.left, minVal, curr.val) and dfs(curr.right, curr.val, maxVal)
            
        return dfs(root, -float("inf"), float("inf")) 
    
# Intuition: When traversing down a node's left subtree, every node in that subtree must be smaller than the current node (i.e. the maxValue decreases) and vice versa for the right subtree. So, every time we traverse left or right we set maxVal or minVal respectively to update the limits for the next node.