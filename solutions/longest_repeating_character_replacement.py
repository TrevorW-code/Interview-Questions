class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # return the len of longest substr containing same letter uppercase
        count = {} # hash of all occuring chars
        res = 0 # max len of sliding window
        l = 0 # left pointer
        maxf = 0 # max word frequency

        for r in range(len(s)): # for each char
            count[s[r]] = 1 + count.get(s[r],0) # add to count of the char, or init at 0
            maxf = max(maxf,count[s[r]]) # get the max between incremented char and maxf

            if (r - l + 1) - maxf > k: # if the sliding window (r - l + 1) is not valid anymore (more edits than k)
                count[s[l]] -= 1 # remove char at left pointer count
                l += 1 # shift window

            res = max(res, r - l + 1) # set the res to the max window
        return res