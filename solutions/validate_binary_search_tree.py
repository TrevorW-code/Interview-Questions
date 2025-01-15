class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left is < middle
        # right is > middle
        # children are not none

        def valid(node: TreeNode, l, r):
            if not node:
                return True
            if not (node.val < r and node.val > l):
                return False
            
            return (
                valid(
                    node.left,
                    l,
                    node.val # new right
                ) and 
                valid(
                    node.right,
                    node.val,
                    r
                ))
        
        return valid(root,float("-inf"),float("inf"))