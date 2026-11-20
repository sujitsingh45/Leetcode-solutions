class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-3):
            #optimization
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                #optimization for duplicate
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=len(nums)-1
                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left=left+1
                        right=right-1
                        #optimization for duplicate
                        while left<right and nums[left]==nums[left-1]:
                            left=left+1
                        while left < right and nums[right] == nums[right+1]:
                            right=right-1
    
                    elif total>target:
                        right=right-1
                    else:
                        left=left+1
        return result                

   #time complexity: for sorting O(nlogn)+n^3
   #space complexity:O(1) and for using the result list to append
        
        