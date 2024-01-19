class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # empty array

            for c in s:
                count[ord(c)-ord('a')] += 1 # at index of character in array
            
            res[tuple(count)].append(s)

        return res.values()