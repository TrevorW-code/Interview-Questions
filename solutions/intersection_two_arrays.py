class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # init counter 
        c = Counter(nums1)
        # counts all of the unique numbers in the list
        
        # init empty list (to return)
        intersect = []
        
        # for number in nums2
        for num in nums2:
            
            # if the number appears more than once in nums1
            if c[num]>0:
                
                # append it to the list
                intersect.append(num)
                
                # detract the counter of that number by 1
                c[num]-=1
        
        return intersect
