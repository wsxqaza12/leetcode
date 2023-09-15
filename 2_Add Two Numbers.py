class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        current = head
        carry = 0

        while l1 is not None or l2 is not None or carry is not 0:

            l1_num = l1.val if l1 is not None else 0
            l2_num = l2.val if l2 is not None else 0

            total = l1_num + l2_num + carry
            current.next = ListNode(total % 10)
            carry = total // 10

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            current = current.next

        return (head.next)
