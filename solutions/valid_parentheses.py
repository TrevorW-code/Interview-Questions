class Solution:
    def isValid(self, s: str) -> bool:

        stack = [] # stack to add most recent paranthese
        
        parenthese_mapping = {
            '}':'{',
            ']':'[',
            ')':'('
        } # hash to check if closed parenthese has open at top of stack

        for char in s: # for each parenthese (assuming no normal chars)
            if char in parenthese_mapping: # if char is closed parenthese
                if stack and stack[-1] == parenthese_mapping[char]: # if a stack exists and the top of stack is mapping to parenthese
                    stack.pop() # remove from stack
                else:
                    return False # break if open and no close in stack
            else:
                stack.append(char) # else add to stack

        return True if not stack else False