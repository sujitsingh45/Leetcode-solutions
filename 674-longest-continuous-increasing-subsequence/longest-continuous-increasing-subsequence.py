class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
         
        if len(nums)==0:
            return 0 #return null if size is null
        k=1  #current subsequence list
        p=1 # maximum subsequence list
        
        
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                k=k+1    
            else:
                k=1
            p=max(p,k)    #updating maximum
        return p      
    
      
        