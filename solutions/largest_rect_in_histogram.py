class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # rectangles must be continuous, all 
        # rectangle can be as large as the smallest side

        # let's get the second greatest "h" and "width"

        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i # start index of h
            while stack and stack[-1][1] > h: # is the current h smaller than the top item on stack
               index, height = stack.pop() # get the index and h of the greater value in stack
               maxArea = max(maxArea, height * (i - index)) # calculate the best rect
               start = index # push index backwards
            stack.append((start,h)) 

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea