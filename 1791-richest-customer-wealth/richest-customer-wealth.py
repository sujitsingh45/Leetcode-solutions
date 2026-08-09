class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest=0
        for customer in accounts:
            wealth=sum(customer) #calculate the sum for every customer 
            if wealth>richest: #update the richest if wealth is more
                richest=wealth
        return richest    
            
        