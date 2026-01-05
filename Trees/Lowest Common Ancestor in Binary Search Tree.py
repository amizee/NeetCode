class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # LCA - two conditions
        # 1. less than p/q and more than p/q - either side of current "root"
        # 2. equal to p/q - LCA is a descendant of itself

        if root.val < q.val and root.val > p.val: # Either side of current node
            return root
        elif root.val < p.val and root.val > q.val: # Either side of current node
            return root
        elif root.val == p.val or root.val == q.val: # Node and left child or node and right child
            return root
        
        # If it reaches this, then both p and q must be on the left or right of the current node
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

# Time complexity: O(h)
# Space complexity: O(h)