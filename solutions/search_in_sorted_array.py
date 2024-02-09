class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1  
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # calc which side you are on
            portion = 'l' if nums[l] <= nums[mid] else 'r'

            if portion == 'l':
                if target > nums[mid] or target < nums[l]: # if the middle value is greater than first element or smaller than target
                    l = mid + 1 # search right
                else:
                    r = mid - 1 # search left
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: 
                    l = mid + 1

            
        return -1