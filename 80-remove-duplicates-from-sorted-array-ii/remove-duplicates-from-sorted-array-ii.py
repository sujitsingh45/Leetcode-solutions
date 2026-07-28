class Solution(object):
    def removeDuplicates(self, nums):
        k=1
        count=1
        for i in range(1,len(nums)): # to go through every element
            if nums[i]==nums[i-1]:# checking if the element is equal to last element
                count=count+1
            else:
                count=1    
            if count <=2:  # we want to same so if 2 or less push
                nums[k]=nums[i]
                k=k+1 

        for p in range(k,len(nums)):  # to get underscore
            nums[p]="_" 
        return k              
        