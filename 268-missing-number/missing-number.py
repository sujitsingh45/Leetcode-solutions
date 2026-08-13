class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        li_sum=0 
        n=len(nums)
        for i in nums:
            li_sum=li_sum+i # calculating the sums


        return (n)*(n+1)//2 - li_sum # return with actual sum with n and given nums's sum

            


        