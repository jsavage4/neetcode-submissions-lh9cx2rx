# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the midpoint
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Sever and reverse the second half
        second = slow.next
        slow.next = None          # sever here, not via a trailing pointer
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3. Interleave
        left, right = head, prev
        while right:              # right is always <= left in length
            next_left = left.next
            next_right = right.next
            left.next = right
            right.next = next_left
            left = next_left
            right = next_right