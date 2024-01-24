class Solution:
    def isPalindrome(self, s: str) -> bool:

        forward = []
        
        for char in s:
            if char not in ",:?;'!()`~%^&*[]{}.@#\"_- ": # this took way too long, just adding interatively
                forward.append(char.lower())
        
        if forward == forward[::-1]:
            return True
        else:
            return False