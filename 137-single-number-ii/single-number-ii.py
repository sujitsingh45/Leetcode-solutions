class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       
        frq={}
        for i in nums:
            if i not in frq:
                frq[i]=1
            else:
                frq[i]+=1
        for k,v in frq.items(): #return when frequency is 1
            if v==1:
                return k            
