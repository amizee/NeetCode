class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        
        carry = False
        while l1 or l2:
            if not l1:
                val = l2.val
            elif not l2:
                val = l1.val
            else:
                val = l1.val + l2.val

            val = val + 1 if carry else val
            if val >= 10:
                carry = True
                val = val % 10
            else:
                carry = False
            curr.val = val

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2:
                curr.next = ListNode()
                curr = curr.next
        
        if carry:
            curr.next = ListNode(1)
        return head

# Intuition: loop through the linked lists and add the digits one by one. Use a "carry" variable to store if the previous sum was over 10.