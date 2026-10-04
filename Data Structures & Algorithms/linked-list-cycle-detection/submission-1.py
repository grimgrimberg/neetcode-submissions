# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        idx = 0
        while head:
            if head not in seen:
                seen.add(head)
                head = head.next
                idx+=1
            else:
                return True
        return False
