class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() # init set
        l = 0 # init l pointer
        res = 0 # init final res var

        for r in range(len(s)): # iterate through list
            while s[r] in char_set: # if char at r in char_set
                char_set.remove(s[l]) # remove it
                l += 1 # and increment left pointer (shift sliding window up)
            char_set.add(s[r]) # 
            res = max(res, r - l + 1)
        return res