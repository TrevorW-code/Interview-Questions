class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init counter as hashmap
        count = {}

        # init frequency bucket sort array
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0) # add 0 + 1 if not exist, otherwise add 1
        for n, c in count.items():
            freq[c].append(n) # add n to freq array at index of it's frequency, c
        
        res = []
        for i in range(len(freq)-1,0,-1): # startbackwards of list
            for n in freq[i]: # for the num in the current index
                res.append(n) # append the num
                if len(res) == k: # once k is reached, complete
                    return res