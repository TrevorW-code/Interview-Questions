class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Set up a point at the 0 index
        left = 0
        
        # for a pointer "right" going throught the numbers
        for right in range(len(nums)):
            
            # if the number is nonzero
            if nums[right]:
                
                # change the index of the numbers at the pointers, switching the value at the right pointer with the zero at the left pointerr
                nums[left], nums[right] = nums[right], nums[left]
                
                # add one to the left pointer, moving it up the index
                left += 1
        
        # return the final array
        return nums
