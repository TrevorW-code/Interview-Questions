class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        
        while q:
            rs = None
            qLen = len(q) # current level
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rs = node
                    q.append(node.left)
                    q.append(node.right)
            if rs:
                res.append(rs.val)
                
        return res