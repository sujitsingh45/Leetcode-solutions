class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i]=nums[j] #swapping the non zero element at the starting 
                i=i+1 #incremnet position


        for j in range(i,len(nums)):
            nums[j]=0  #0 on the remaining place 


       #time complexity:O(n)
       #space complexity:0(1)     



        

        """
        Do not return anything, modify nums in-place instead.
        """
        