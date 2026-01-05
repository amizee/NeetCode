class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(root_val)
            index = indices[root_val]
            node.left = dfs(l, index - 1)
            node.right = dfs(index + 1, r)

            return node
            
        return dfs(0, len(inorder) - 1)

# Preorder array determines the order each node should be created
# Inorder array determines whether a node is on the left or right subtree of a root node
# Intuition: Recursively build the left and right subtrees using DFS by splitting the range [l, r] into two parts for its left and right subtree and creating a new node in each call
# The indices for inorder are pre-calculated to achieve O(n) time