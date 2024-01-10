class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l = 1 # left pointer to reference index

        for r in range(1,len(nums)): # right pointer to scan through loops
            if nums[r] != nums[r - 1]: # if previous num is not the same as current num
                nums[l] = nums[r] # update num at l pinter in place
                l += 1 # incremement l
        return l 