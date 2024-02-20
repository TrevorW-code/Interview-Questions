class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return "" # edge case

        countT, window = {}, {} # init empty hash
        for c in t:
            countT[c] = 1 + countT.get(c,0)

        have, need = 0, len(countT) # init int shortcuts for comparing hash maps

        res, resLen = [-1,-1], float('inf') # init res (two pointers), and len of res
        l = 0 # init left pointer
        
        for r in range(len(s)): # right pointer iterates through code
            c = s[r] # get char
            window[c] = 1 + window.get(c,0) # update count in current window

            if c in countT and window[c] == countT[c]: # if char in required countT, and counts are equal in both hashs
                have += 1 # update the have!

            while have == need: # while you have the chars you need in the substring
                if (curLen := r - l + 1) < resLen: # if the current window substring is smaller than resLen
                    res = [l, r] # get the pointers together
                    resLen = curLen # update the best len to smaller window len

                window[s[l]] -= 1 # pop left most val from window hash
                
                # if popped character was in countT, and the count is now less than required
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1 # update shortcut
                l += 1
        
        resl,resr = res
        
        return s[resl:resr+1] if resLen < float('inf') else ""
            