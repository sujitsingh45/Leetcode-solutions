class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum=[0]*len(nums)
        prefixsum[0]=nums[0]
        count=0

        for i in range(1,len(nums)):
            prefixsum[i]=prefixsum[i-1]+nums[i]
        #now create a map
        dict1={}
        for j in range(len(nums)):
            if prefixsum[j]==k:
                count=count+1
            val=prefixsum[j]-k
            if val in dict1:
                count+=dict1[val] #adding frequency
            #storing  in hashmap    
            if prefixsum[j] in dict1:
                dict1[prefixsum[j]] += 1
            else:
                dict1[prefixsum[j]] = 1  
    
      
           
        return count





        
        
                           
        
        