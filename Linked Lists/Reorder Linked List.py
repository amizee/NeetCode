class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the halfway point 
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # Right half that needs to be reversed can be smaller than the left half
        slow.next = None # "Splits" the list in half
        # Reverse the second half of the list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1
            first, second = tmp1, tmp2

# Intuition: Reverse the right half, then merge the two halves into one list