# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one = head
        two = head
        if not head.next:
            return None
        while two and two.next:
            pre = one
            one = one.next
            two = two.next.next

        pre.next = one.next

        return head
