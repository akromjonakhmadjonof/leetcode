# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        dummy = ListNode()
        current = dummy

        while head:
            if (head.next and head.val == head.next.val) or (head.val in seen):
                seen.add(head.val)
            else:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        return dummy.next