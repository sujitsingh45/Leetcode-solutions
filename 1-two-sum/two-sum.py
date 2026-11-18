class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
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

        