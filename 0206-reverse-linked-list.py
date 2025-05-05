# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        current = head

        while current and current.next:
            temp = current.next
            if temp.val == val:
                current.next = temp.next
            else:
                current = current.next

        return head
