class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        seen_vals = {}

        for num in nums:
            if num in seen_vals.keys():
                return True
            else:
                seen_vals[num] = 1
        return False