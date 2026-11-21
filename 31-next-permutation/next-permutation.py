class Solution:
    def nextPermutation(self, nums: list[int]) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """
        #find the pivot
        n=len(nums)
        piv=-1
        for i in range(1,n):
            if nums[-i]>nums[-i-1]:
                piv=n-i-1 # we want the index
                break
        if piv==-1:
            nums.reverse()#reversing the entire list
            return  
        #next larger element to pivot
        for i in range(n-1,piv,-1):
            if nums[piv]<nums[i]:
                temp=nums[i]
                nums[i]=nums[piv]
                nums[piv]=temp
                break   

        #third step to reverse the element from pivot+1 to n-1
        #use while loop
        left=piv+1
        right=n-1
        while left<right:
            temp=nums[left]
            nums[left]=nums[right]
            nums[right]=temp
            left=left+1
            right=right-1  


#time complexity:O(n)
#space complexity:O(1)