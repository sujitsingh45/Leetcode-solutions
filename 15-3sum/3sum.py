class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)-2):  #choosing the first value and not duplicate
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    result.append([nums[i],nums[left],nums[right]])
                    left=left+1
                    right=right-1
                    while left<right and nums[left]==nums[left-1]: #not taking duplicate
                        left=left+1
                    while left<right and nums[right]==nums[right+1]:#not taking duplicate
                        right=right-1

                elif total>0:
                    right=right-1
                else:
                    left=left+1
        return result

        #time complexity:O(n)
        #space complexity:O(k)






       
                

    
        
        