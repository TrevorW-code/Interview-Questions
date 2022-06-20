# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # set up pointers previous and current
        prev, curr = None, head
        
        # while there is a current value
        while curr:
            
            # save a temporary value of the next item in the linked list
            nxt = curr.next
            
            # swap the positions of the next item and the previous item
            curr.next = prev
            prev = curr
            
            # set the set current item to the nex actual item saved in the temporary variable
            curr = nxt
        
        # return
        return prev
