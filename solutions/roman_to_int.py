class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        total = 0
        
        for current in range(len(s)): # going through index of list
            if current + 1 < len(s) and roman[s[current]] < roman[s[current+1]]:
                total -= roman[s[current]]
                continue
            total += roman[s[current]]
        
        return total
