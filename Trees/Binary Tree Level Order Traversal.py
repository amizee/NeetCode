from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        
        if root:
            queue.append(root)

        while len(queue) > 0:
            subList = []
            for i in range(len(queue)):
                node = queue.popleft()
                subList.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(subList)

        return res
    
# Standard breadth first search using a deque