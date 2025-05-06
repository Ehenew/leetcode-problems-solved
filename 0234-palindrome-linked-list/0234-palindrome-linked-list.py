# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes_list = []
        temp = head        
       
        while temp is not None:
            nodes_list.append(temp.val)
            temp = temp.next

        return nodes_list == nodes_list[::-1]