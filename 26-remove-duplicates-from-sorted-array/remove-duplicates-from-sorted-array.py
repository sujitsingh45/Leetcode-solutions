class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start=1 # count the number of element after extracking
        #if length is 1 return 
        n=len(nums)
        if n==1:
            return 1
        for i in range(1,n):
            if nums[i-1]!=nums[i]:
                
                nums[start]=nums[i] #take elemnt after removal of duplicaton
                start+=1

        for j in range(start,n-1):
            nums[j]="_"
            
        return start          


        