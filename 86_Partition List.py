# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head

        small_end = ListNode(0)
        large_end = ListNode(0)
        small_head = small_end
        large_head = large_end

        while head:
            if head.val < x:
                small_end.next = head
                small_end = head
            else:
                large_end.next = head
                large_end = head
            head = head.next


        large_end.next = None
        small_end.next = large_head.next
        return small_head.next
    
# 上為優化
        # if head is None:
        #     return head
            
        # small_ls = ListNode(None)
        # large_ls = ListNode(None)
        # ans = ListNode(None)
        # large_head = ListNode(None)

        # while head:
        #     if head.val < x:
        #         small_ls.next = head
        #         if small_ls.val is None:
        #             ans = head
        #         small_ls = head
        #     else:
        #         large_ls.next = head
        #         if large_ls.val is None:
        #             large_head = head
        #         large_ls = head
        #     head = head.next


        # large_ls.next = None
        # if small_ls.val is None:
        #     return large_head
        # else:
        #     small_ls.next = large_head if large_head.val is not None else None
        #     return ans