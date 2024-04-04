# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True # because a null is a child of TreeNode
        if not root: return False # if there is a subroot but no root, can't be sub tree

        if self.sameTree(root,subRoot):
            
            return True
        
        return (
            self.isSubtree(root.left,subRoot)
            or
            self.isSubtree(root.right,subRoot)
        )

    def sameTree(self, s, t):
        if not s and not t: # if both nodes don't exist they are equal
            
            return True
        
        if s and t and s.val == t.val: # keep going until rejected
            
            return (
                self.sameTree(s.left, t.left)
                and
                self.sameTree(s.right, t.right)
            )

        return False # return False if rejected