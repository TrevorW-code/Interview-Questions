class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet: # if the smaller value doesn't exist, i.e. beginning of a sequence
                length = 0
                while (n + length) in numSet: # see if the bigger values exist
                    length += 1 # add length of list + 1
                longest = max(length,longest) # get whichever is bigger
        return longest