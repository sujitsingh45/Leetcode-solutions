class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        i=0
        for j in range(len(nums)-1): #array simulation work
            if nums[j+1]==nums[j]:
                nums[j]=nums[j]*2
                nums[j+1]=0
        for j in range(len(nums)):   #all non zero element at one palace       
            if nums[j]!=0:
                nums[i]=nums[j]
                i=i+1

        for j in range(i,len(nums)): #all zero at the last
            nums[j]=0
        return  nums

        #time complexity:O(n)
        #space complexity:O(1)


        