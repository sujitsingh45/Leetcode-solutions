class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using two pointers
        left=0
        right=len(nums)-1
        while left<right:
            sum1=nums[left]+nums[right]
            if sum1==target: #return if equal to target
                return [left+1,right+1] 
            elif sum1>target:  #if greater deacrement right 
                right-=1
            else: # else increment left
                left+=1 


    '''n=len(numbers)
        di_ct={}
        for i in range(n):
            rem=target-numbers[i]
            if rem in di_ct:
                return [di_ct[rem]+1,i+1]
            di_ct[numbers[i]]=i '''
     #time complexity:O(n)
     #space complexity:O(1)
        