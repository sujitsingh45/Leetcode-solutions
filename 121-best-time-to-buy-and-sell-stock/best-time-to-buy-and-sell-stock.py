class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices=prices[0] #taking first as minimum
        profit=0 # take maximum as 0 and update it
        for i in range(1,len(prices)):
            curr_profit=prices[i]- min_prices
            if curr_profit>profit:
                profit=curr_profit #updating the profit
            min_prices=min(min_prices,prices[i]) #taking the min to buy
        return profit        



        

        