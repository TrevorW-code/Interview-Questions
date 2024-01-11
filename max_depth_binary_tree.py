# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # pre-order iterative dfs
        stack = [[root,1]] # node + depth
        res = 0 # storing maximum depth

        while stack:
            node, depth = stack.pop()

            if node: # ignore null nodes
                res = max(res,depth) # get the higher value between the current max depth and node popped's depth
                stack.append([node.left,depth + 1]) # adding lower node childen (even in null)
                stack.append([node.right,depth + 1]) # adding lower node childen (even in null)
                
        return res