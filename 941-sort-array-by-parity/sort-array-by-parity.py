class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """ even=[] #store even element
        odd=[] #store odd element
        n=len(nums)
        if n==1:  # return if len is 1
            return nums
        for i in range(0,n):
            if nums[i]%2==0:
                even.append(nums[i]) #append if sum
            else:
                odd.append(nums[i]) #append if odd    

        return even+odd  """
      
#by swapping the element and not using extra variable
        n=len(nums)
        if n==1:
            return nums
        start=0
        for i in range(n):    
           if nums[i]%2==0:
            temp=nums[i]
            nums[i]=nums[start]
            nums[start]=temp
            start+=1
        return nums    

        