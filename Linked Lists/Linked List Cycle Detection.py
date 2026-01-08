class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Intuition: fast and slow pointers - if there's a cycle the fast pointer will eventually "catch" the slow pointer because it gains 1 on it every iteration