# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #initialization
        #dummy is a list which has its first node to be null
        dummy = current = ListNode() 
        #edge cases:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # actual logic starts here
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
            # when one of the list still has remaining nodes
            if list1 is None:
                current.next = list2
            else:
                current.next = list1
                
        return dummy.next  # the list "dummy" starts with dummy.next
                