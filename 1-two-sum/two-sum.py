class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        #hashing aproach
        dict1={}
        for i in range(len(nums)):
            first=nums[i]
            second=target-first
            if second in dict1:
                return [dict1[second],i]
            else:

                dict1[nums[i]]=i  

        '''
        #two pointer approcah
       arr=[(num,index)for index,num in enumerate(nums)]
       arr.sort()
       left=0
       right=len(arr)-1
       while left<right:
        curr_sum=arr[left][0]+arr[right][0]
        if curr_sum==target:
            return[arr[left][1], arr[right][1]]
        if curr_sum>target:
            right=right-1
        else:
            left=left+1
            '''


        