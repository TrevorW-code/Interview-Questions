class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False # can't find permutation if too large

        # init windows
        s1Count, s2Count = [0] * 26, [0] * 26 # storing vals in array instead of hash
        for i in range(len(s1)): # went quickly through s1 first
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # init matches
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0) # increment if same otherwise don't

        l = 0
        for r in range(len(s1),len(s2)): # pick back up at next array
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]: # check if they are equal
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]: # incremented too far
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]: # check if they are equal
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]: # incremented too far
                matches -= 1

            l += 1
        
        return matches == 26

