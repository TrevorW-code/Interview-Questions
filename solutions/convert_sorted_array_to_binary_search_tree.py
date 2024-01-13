# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def tree_helper(l,r): 
            if l > r: # left most pointer should never be greater than right pointer
                return None

            m = (l+r) // 2 # get mid pointer of sub array
            root = TreeNode(nums[m]) # create the root at the middle of the sub array
            root.left = tree_helper(l,m-1) # move right pointer below mid
            root.right = tree_helper(m+1,r) # move left pointer above mid

            return root

        return tree_helper(0,len(nums)-1)