class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = {} # empty hash
        
        for num in nums: # for each num
            if num not in counter:
                counter[num] = 1 # instantiate if not exist
            else:
                counter[num] = counter[num] + 1 # add if exists
        
        maj_element = 0
        max_occur = 0
        
        for num, occurances in counter.items(): # for items in dict
            if occurances > max_occur: # if nums occurances > max_occur
                max_occur = occurances # update max_occur
                maj_element = num # update maj element
        
        return maj_element