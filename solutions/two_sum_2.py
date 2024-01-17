class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # hash map
        mapping = {}

        for idx, num in enumerate(nums): # get index and num
            needed_val = target - num # get the value needed to complete problem
            if needed_val in mapping: # if the value exists in the mapping
                return [mapping[needed_val],idx] # grab the index from the mapping
            else: 
                mapping[num] = idx # otherwise add the mapping to the index


        

        