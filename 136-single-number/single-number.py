class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #bit manipulation
        a=0             #xzor function
        for x in nums:         # 0+0=0
            a^=x                #0+1=1 
        return a                #1+0=1
                                #1+1=0 
        #time complexity:O(n)
        #space complexity:O(1)    
        



        