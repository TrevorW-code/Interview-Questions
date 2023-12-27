class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # set cheapest price to highest
        cheapest_price = float('inf')

        # best profit margin initialized
        best_margin = 0

        # for each price in the prices
        for price in prices:

            # if cheapest price is greater than current price
            if cheapest_price > price:
                
                # set new cheapest price 
                cheapest_price = price
            
            # set current_margin 
            current_margin = price - cheapest_price
            
            # if the current_margin is greater than the best_margin
            if current_margin > best_margin:
                
                # set the new best margin
                best_margin = current_margin

        # return the best margin
        return best_margin