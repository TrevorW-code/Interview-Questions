class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)] # get a list of car pairs (position, speed)

        stack = [] # create a stack to hold the fastest car
        for p, s in sorted(pair)[::-1]: # reverse the sort, sorts by the first key (position)
            stack.append((target - p) / s) # calculate the time it would take for the car to reach target
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # if there are two cars in the stack and the car further back gets their faster
                stack.pop() # remove the faster, further back car because it will be limited by the slow one anyways.
        
        return len(stack)