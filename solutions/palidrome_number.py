class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ans = False
        if str(x) == str(x)[::-1]:
            ans = True
        return ans
