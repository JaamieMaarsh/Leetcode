# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # this is a DFS prob since we are finding the height:
        balanced = [True]
        def height(root):
            # base case
            if root is None:
                return 0 #shouldnt contribute to the height

            # finding the height of the nodes
            left_height = height(root.left)
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                #return 0
            return 1+max(left_height, right_height)
        height(root)
        return  balanced[0]           
        


