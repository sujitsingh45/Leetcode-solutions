class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy=prices[0] #to get minimum buy day
        max_profit=0
        for i in range(1,len(prices)):
            #taking best day to buy
            best_buy=min(best_buy,prices[i])
            #calculating profit
            if prices[i]>best_buy:
                max_profit=max(max_profit,prices[i]-best_buy) 
            
        return max_profit     #return max profit       
        
        #time complexity:O(n)
        #space complexity:O(1)





      


        

        