class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # check if the next temp is higher than current. If is, add one. Else, add
        stack = [] # pair at stack
        res = len(temperatures) * [0] # init full list

        for i, t in enumerate(temperatures): # index and temperature
            while stack and t > stack[-1][0]: # while the stack still has items and the most recent temperature is greater than the top of the stack
                stackT, stackIdx = stack.pop()  # take out the temp data from stack
                res[stackIdx] = (i - stackIdx) # for the result at the stack index, add the difference between the current index and the stored temperature index
            stack.append([t, i]) # add the most recent temp data to stack
        return res # return result