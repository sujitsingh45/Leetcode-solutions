class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0 
        n=len(prices)
        for i in range(n-1):
            if prices[i+1]>prices[i]: #buyin if it's less
                profit+=prices[i+1]-prices[i] #adding the profit after sell

        return profit       
        