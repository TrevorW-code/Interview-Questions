# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # create dummy node for avoid inserting into empty list
        dummy = ListNode()
        
        # first node in our list is this empty node 
        tail = dummy
        
        # while list1 and list2 are not empty
        while list1 and list2:
            
            # if list1 node is smaller than list2 node
            if list1.val < list2.val:
                
                # set current list1 node to the next tail node
                tail.next = list1
                
                # then update list1 pointer
                list1 = list1.next
                
            # otherwise
            else:
                
                # set current list2 node to the next tail node
                tail.next = list2

                # then update list2 pointer
                list2 = list2.next
            
            # set current tail node to whichever next node was inserted
            tail = tail.next
            
        # in the cases that one of the node lists is longer, set whichever node list longer to the next node
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # return the entire nodelist
        return dummy.next
            
