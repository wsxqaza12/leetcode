# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):

        dummy_ListNode = ListNode(0)
        dummy_ListNode.next = head
        pre = dummy_ListNode
        current = head

        while current:

            while current.next and current.val == current.next.val:
                current = current.next
            
            if pre.next == current:
                pre = pre.next
                current == current.next
            else:
                pre.next = current.next
                current = current.next
                
        return dummy_ListNode.next