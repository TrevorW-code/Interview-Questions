class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # deque
        l = r = 0 # init both pointers to 0

        while r < len(nums): # while r is not at the end of the nums
            while q and nums[q[-1]] < nums[r]: # while smaller values exist in our queue
                q.pop() # pop the smaller values at the end
            q.append(r) # append the new val

            if l > q[0]: # if our left pointer is out of bounds in our window
                q.popleft() # remove left val from window
            
            if (r + 1) >= k: # have to make sure the window is at least size k
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output

