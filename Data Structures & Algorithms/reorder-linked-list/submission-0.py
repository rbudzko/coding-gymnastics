# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            fast = fast.next

        left, right = head, fast

        prev = None
        curr = slow
        while curr != right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        right.next = prev

        head = left
        curr = head
        left = left.next
        while right and left:
            curr.next = right
            right = right.next
            curr = curr.next
            curr.next = left
            left = left.next
            curr = curr.next
        
        if right: 
            curr.next = right
            curr = curr.next
        
        curr.next = None