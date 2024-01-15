class Solution:
    def climbStairs(self, n: int) -> int:

        # Dynamic Programming!
        # Essentially fib sequence, v cool

        one, two = 1,1 # init both pointers to one

        for i in range(n-1):
            temp = one # save first pointer temporararily
            one = one + two # update first pointer with sum of first and second
            two = temp # update second pointer to og value of first

        return one # return final step count