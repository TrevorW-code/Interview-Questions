class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles) # biggest item
        low = min(piles) # smallest item
        best_speed = high

        while low <= high:
            speed_guess = (low + high) // 2

            # test eating
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / speed_guess)
            
            if hrs <= h:
                best_speed = min(best_speed,speed_guess)
                high = speed_guess - 1
            else:
                low = speed_guess + 1
        
        return best_speed