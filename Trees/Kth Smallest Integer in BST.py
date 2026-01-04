class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(curr):
            if not curr:
                return
            
            dfs(curr.left)
            res.append(curr.val)
            dfs(curr.right)
        
        dfs(root)
        return res[k - 1]

# Intuition: Inorder traversal from left -> node -> right. Can't return early out of the DFS so we store the order in an array and return the k-1th element.