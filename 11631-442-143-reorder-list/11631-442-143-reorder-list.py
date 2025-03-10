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
        # finding the midpoint
        slow = fast = head

        # 1 -> 2 -> 3 -> 4 
        # s
        # f
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        List2 = slow.next
        slow.next = None

        # reverse list 2
        prev = None

        while List2:   # 3 -> 4 -> 5
            temp = List2.next
            List2.next = prev
            prev = List2
            List2 = temp
        List2 = prev
        
        # Now, I have 2 lists in the same order
        List1 = head

        while List1 and List2:
            List1next = List1.next
            List2next = List2.next
            List1.next = List2
            List2.next = List1next
            List1 = List1next
            List2 = List2next

        


        