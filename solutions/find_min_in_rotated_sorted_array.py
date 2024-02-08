class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # start res at the left most value

        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]: # if we get to a correctly sorted portion
                res = min(res, nums[l]) # just grab the smaller value between left pointer and current res
                break
            
            m = (l + r) // 2 # get mid point
            res = min(res, nums[m]) # take the min between the res and the mid point
            
            # now check if this value is part of the left sorted portion
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return res