class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        
        node, prev = head, head
        index = length - n
        # If the head is removed
        if index == 0:
            return head.next

        # Loop to the node being removed and set prev.next -> node.next
        for i in range(index):
            prev = node
            node = node.next
        prev.next = node.next
        
        return head

# Intuition: Calculate the index of the node being removed and swap pointers.