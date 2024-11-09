# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        
        current = head
        prev = None
        
        while current:
            Cnext = current.next
            current.next = prev
            prev = current
            current = Cnext
        return prev
        