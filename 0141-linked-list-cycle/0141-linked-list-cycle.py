# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        existing_nodes = set()
        current_node = head
        
        while current_node:
            if current_node in existing_nodes:
                return True
            else:
                existing_nodes.add(current_node)
                current_node = current_node.next
        return False