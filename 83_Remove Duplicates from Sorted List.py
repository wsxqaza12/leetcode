# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            next = current.next
            if current.val == next.val:
                current.next = next.next
                continue
            
            current = next

        return head
        