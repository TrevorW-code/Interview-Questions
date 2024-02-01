class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] # to hold the current amount of strings
        res = [] # to hold the correct combinations of the stack

        def backtrack(openN,closedN): # recursive func using the count of open and closed parenthesis
            if openN == closedN == n: # if the open and closed counts of parenthesis are equal to n
                success_case = "".join(stack)
                print(f'adding {success_case}')
                res.append("".join(stack)) # add this combination of open and closed parenthesis
                return # end func
            if openN < n: # if you can still add another parenthesis
                stack.append("(") # append open parenthesis 
                backtrack(openN + 1, closedN) # continue recursion w added to openN
                stack.pop() # update stack by removing previous add
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return res