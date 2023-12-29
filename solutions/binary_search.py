class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # setup pointers to track edges of searched part of array
        left, right = 0, len(nums) -1

        # while left and right are not the same
        while left <= right:

            # get the mid point
            mid = (left + right) // 2

            # target is in lower half
            if nums[mid] > target: 
                
                # move right to mid point
                right = mid - 1
            
            # target is in upper half
            elif nums[mid] < target: 
                
                # move left to mid point
                left = mid + 1
            
            else:

                # if left and right are the same index, 
                return mid
        
        return -1