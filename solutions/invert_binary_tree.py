# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp = root.left # save left
        root.left = root.right # set l to r
        root.right = tmp # set r to saved node at l

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root