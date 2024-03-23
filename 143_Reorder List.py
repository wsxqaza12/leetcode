# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        record = []
        while head:
            record.append(head)
            head = head.next

        n = len(record)
        if n % 2 == 0:
            times = n/2
        else:
            times = n//2 + 1

        ans = ListNode(None)
        dummy = ans

        for i in range(int(times)):
            print(i, n)
            dummy.next = record[i]
            dummy = dummy.next
            if n > i:
                print("n", n)
                dummy.next = record[n-1]
                dummy = dummy.next
                n -= 1

        dummy.next = None
        return ans.next
