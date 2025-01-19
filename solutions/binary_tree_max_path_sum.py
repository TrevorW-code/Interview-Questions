# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # start at the bottom of the tree, lets go left
        res = [root.val]

        def dfs(root: TreeNode):
            if not root:
                return 0
            
            # handle negatives + dfs on l & r nodes
            lm = max(dfs(root.left), 0)
            rm = max(dfs(root.right), 0)

            # max w split
            res[0] = max(res[0],root.val + lm + rm)

            # max w/o split
            return root.val + max(lm,rm)

        dfs(root)
        return res[0]