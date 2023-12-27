class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    
        # number of nodes, init to inf
        prices = [float('inf')] * n
        
        # starting node is cost 0
        prices[src] = 0

        # looping through the number of stops
        for i in range(k+1):
            
            # make copy of price
            tmpPrices = prices.copy()

            # src, dest, price
            for s, d, p in flights: 
                
                # if src is impossible to get to
                if prices[s] == float('inf'): 
                    continue
                
                # if price at source + price of current flight is less than temp prices, update
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
                    print(tmpPrices)

            # update prices
            prices = tmpPrices

        # if not found, return -1
        return -1 if prices[dst] == float('inf') else prices[dst]
    


        