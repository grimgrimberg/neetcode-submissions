# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head

        # 1 create gap of n nodes
        for _ in range(n):
            fast = fast.next
        #2 ede case, if n is len lest, delete head
        if not fast:
            return head.next
        #3 slide both pointes until fast reaches end
        while fast.next:
            slow = slow.next
            fast = fast.next
        #4 skip target node
        slow.next = slow.next.next
        return head
        # if not head:
        #     return
        # slow,fast = head,head.next
        # for i in range(n):
        #     while fast:
        #         slow = slow.next
        #         fast = fast.next
        #         if i == n:
        #             slow.next = fast.next
        # return head