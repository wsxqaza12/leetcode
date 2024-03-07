# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check_num = head
        num = 0

        while check_num:
            num += 1
            check_num = check_num.next

        if num % 2 != 0:
            middle = num//2 +1
        else:
            middle = num/2 + 1

        for _ in range(int(middle)-1):
            head = head.next

        return head
