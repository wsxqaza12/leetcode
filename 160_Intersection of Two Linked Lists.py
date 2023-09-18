# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dummyA = headA
        dummyB = headB
        length_A = 0
        length_B = 0

        while dummyA:
            length_A +=1
            dummyA = dummyA.next

        while dummyB:
            length_B +=1
            dummyB = dummyB.next

        if length_A > length_B:
            for _ in range(length_A-length_B):
                headA = headA.next

        if length_A < length_B:
            for _ in range(length_B-length_A):
                headB = headB.next


        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None

## Hashset
        # num_set = set()
        # current = headA

        # while current:
        #     num_set.add(current)
        #     current = current.next
        
        # current = headB
        # while current:
        #     if current in num_set:
        #         return current
        #     current = current.next
        
        # return None