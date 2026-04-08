# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        targetNode = length - n + 1
        count = 0
        curr = head
        prev = None
        while curr:
            count += 1
            if count == targetNode:
                if prev == None:
                    return curr.next
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
        
        return head
