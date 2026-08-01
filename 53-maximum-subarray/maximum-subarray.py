class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:# if the size is one
            return nums[0]
        curr_sum=0
        max_sum=nums[0]
        for i in range(n):
            curr_sum+=nums[i]
            if curr_sum>max_sum:
                max_sum=curr_sum #upadating the maximum sum in sub array
            #when sum is negative
            if curr_sum<0:
                curr_sum=0
        return max_sum            