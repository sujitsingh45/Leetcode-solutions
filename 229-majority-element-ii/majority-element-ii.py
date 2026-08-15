class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        candidate1=None
        candidate2=None
        count1=0
        count2=0
        for num in nums:
            if num==candidate1:  
                #count if its equal
                count1=count1+1
            elif num==candidate2:
                #count if its equal
                count2=count2+1
                #assign if count is zero
            elif count1==0:
                candidate1=num
                count1=1
            elif count2==0:
                candidate2=num
                count2=1 
            #decrease if condition dosen't satisfy
            else:
                count1-=1
                count2-=1
        #verifying for both the candidate        
        result=[]
        if nums.count(candidate1)>len(nums)//3:
            result.append(candidate1)
            #if both not equal and its greater than length//3 then append
        if candidate1!=candidate2 and nums.count(candidate2)>len(nums)//3:
            result.append(candidate2)
        return result   

            