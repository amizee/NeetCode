class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        nodes = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            nodes[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            nodes[curr].next = nodes.get(curr.next, None)
            nodes[curr].random = nodes.get(curr.random, None)
            curr = curr.next
        return nodes[head]

# Intuition: a single pass doesn't work because the random pointer might point to a node later in the list that hasn't been created yet.
# Loop through the original list and create a new node copy mapped by the original node reference. (old node: new node) Now the hashmap contains all the copies.
# A second loop to set the correct pointers as we have access to all the node copies, and since they're object references they'll all get updated.