class Solution:   

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False    

        if not root:
            return False
    
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
# Intuition: isSameTree() - if both trees are null then you've reached a leaf node and this entire subtree is equal, otherwise both p and q need to be non-null and equal the same value or the subtree is not equal. (i.e. different values or one null and one non-null)
# Simply, DFS through each node once and check if the subRoot is rooted at this node with the same structure and node values