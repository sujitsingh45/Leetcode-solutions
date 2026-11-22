class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day=prices[0] #to get minimum buy day
        max_profit=0
        for i in range(1,len(prices)):
            #taking best day to buy
            buy_day=min(buy_day,prices[i])
            #calculating profit
            profit=prices[i]-buy_day
            if profit>max_profit: #compare and update profit
                max_profit=profit
        return max_profit     #return max profit       
        
        #time complexity:O(n)
        #space complexity:O(1)





      


        

        