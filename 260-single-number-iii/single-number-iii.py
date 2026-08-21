class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n==2:
            return nums
        x=[]    
        frq={}
        for i in range(n):
            if nums[i] not in frq:
                frq[nums[i]]=1
            else:
                frq[nums[i]]+=1
        for k,v in frq.items():
            if v==1:
                x.append(k)
        return x                        
        