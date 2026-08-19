class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        frq={}
        for i in nums: #calculate the frequency of each element
            if i not in frq:
                frq[i]=1
            else:
                frq[i]+=1
        for key,val in frq.items():
           # if frequency is greater or eqaul to 2 return
            if val>=2:
                return key         
        

        