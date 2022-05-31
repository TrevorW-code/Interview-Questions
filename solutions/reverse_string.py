class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # define a left and right index
        left, right = 0, len(s)-1
        
        # while the indexes are not equal
        while left<right:
            
            # assign the left and right indexes the value of the right and left index, respectively
            s[left],s[right] = s[right],s[left]
            
            # increment the left pointer, and decrement the right pointer
            left, right = left + 1, right - 1
