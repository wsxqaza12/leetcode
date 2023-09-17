# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):

        if head is None or head.next is None:
             return head

        dummy_ListNode = ListNode()
        pre = dummy_ListNode
        current = head

        while current is not None and current.next is not None:
            pre.next = current.next
            current.next = current.next.next
            pre.next.next = current

            pre = current
            current = current.next   
        return dummy_ListNode.next