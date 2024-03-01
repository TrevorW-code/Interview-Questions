"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None : None} # mapping to save new and old nodes. Handles "random" pointer

        cur = head # get the head
        while cur: # while node exists
            copy = Node(cur.val) # make a copy with associated node val
            oldToCopy[cur] = copy # set that copy in hashmap
            cur = cur.next # go to next node

        cur = head # second pass! get the head node
        while cur: # while node exists
            copy = oldToCopy[cur] # get the copy
            copy.next = oldToCopy[cur.next] # get the next node using the old one
            copy.random = oldToCopy[cur.random] # get the random node using the old one
            cur = cur.next # new current node

        return oldToCopy[head]