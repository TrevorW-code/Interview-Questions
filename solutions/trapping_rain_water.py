class Solution:
    def trap(self, height: List[int]) -> int:
        # Tricky problem, will need to review
        if not height: return 0 # handle edge case

        l, r = 0, len(height)-1 # set pointers
        lmax, rmax = height[l],height[r] # init maxes
        res = 0 # init final result

        while l < r: # while pointers haven't crossed
            if lmax < rmax: # if lmax is less than rmax
                l += 1 # shift left pointer
                lmax = max(lmax,height[l]) # update lmax if new max is found
                res += lmax - height[l] # subtract the max from the height of the left pointer to get water at that point
            else: # otherwise
                r -= 1 # shift right pointer
                rmax = max(rmax,height[r]) # update rmax if new max is found
                res += rmax - height[r] # subtract the max from the height of the right pointer to get water at that point
        
        return res
            


