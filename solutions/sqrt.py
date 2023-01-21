class Solution:
    def mySqrt(self, x: int) -> int:
        

        # defining variables left and right
        l, r = 0, x
        
        # while left is less than or equal to right
        while l <= r:

            # the middle value is the two left and right pointers split in the middle
            m = (l+r)//2

            # if the middle pointer is less than or equal to the input
            if (m*m<=x):

                # return the left pointer as the middle pointer plus one
                l = m+1
            else:

                # return the right pointer as the middle pointer minus one
                r = m-1
        
        return r