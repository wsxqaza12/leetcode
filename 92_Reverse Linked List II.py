# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(-1, head)
        left_end = dummy

        for _ in range(left-1):
            left_end = left_end.next
        
        curr = left_end.next
        reverse_end = curr

        prev = None
        for _ in range(right - left+1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        left_end.next = prev
        reverse_end.next = curr

        return dummy.next
    