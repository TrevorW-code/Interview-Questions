class Solution:
    def maxArea(self, height: List[int]) -> int:
        # find the maximum area rectangle
        # distance between idx = width
        # max height is highest and second highest value.

        max_area = 0

        # start the pointers
        l, r = 0, len(height) - 1

        # calculate the area of the first two idx
        while l < r:
            rec_width = r - l
            rec_height = min(height[l],height[r])
            curr_area = rec_width * rec_height
            if curr_area > max_area:
                max_area = curr_area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1