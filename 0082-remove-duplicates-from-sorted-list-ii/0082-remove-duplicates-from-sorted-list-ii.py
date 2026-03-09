# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        previous = dummy

        while previous.next:
            current = previous.next
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                previous.next = current.next
            else:
                previous = previous.next

        return dummy.next