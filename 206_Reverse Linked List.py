# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        current = head
        pre = None

        while current:
            next = current.next

            current.next = pre
            
            pre = current
            current = next

        return pre

# 2024/03/21 daily