class Solution:
    def firstUniqChar(self, s: str) -> int:
        # slow as possible lol

        final_index = float('inf') # make a infinite index

        for idx,char in enumerate(s): # iterate through characters
            if s.count(char) > 1: # if character appears more than 1
               continue # skip
            else:
                final_index = idx if idx < final_index else final_index # otherwise return index if less than current "final index"

        if final_index == float('inf'): # convert to -1 if unchanged
            return -1 
        
        return final_index
