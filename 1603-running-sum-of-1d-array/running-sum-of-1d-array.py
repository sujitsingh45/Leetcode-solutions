class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #loop to get sum of all the element
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]  #adding the element by the index
        return nums    
        