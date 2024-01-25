class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers)-1 # create pointers for beginning and end of array

        while l < r: # while pointers don't cross
            curSum = numbers[l] + numbers[r] # current sum is nums at l and r pointer index

            if curSum > target: # if the current sum is greater than the target
                r -= 1 # decrement right pointer, which is higher on the sorted list
            elif curSum < target: # if the current sum is less than the target
                l += 1 # incremement the left pointer, which is lower on the sorted list
            else:
                return [l+1,r+1] # otherwise, edgecase met, reuturn

        return [] # handle any exceptions