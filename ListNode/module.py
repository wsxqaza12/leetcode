class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def check_ListNode_ans(head):
    while head:
        print(head.val)
        head = head.next

def array_to_ListNode(arr):
    ls = ListNode(-1)
    dummy = ls

    for i in range(len(arr)):
        temp_node = ListNode(arr[i])
        dummy.next = temp_node
        dummy = dummy.next
    return ls.next
