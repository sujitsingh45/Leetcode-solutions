class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=None #first candidate is none
        count=0
        for num in nums:
            if count==0:
                candidate=num #initialize the first element as candidtae 
            if num==candidate:
                count=count+1 # add if equal
            else:
                count=count-1
        return candidate  #return the present candidate after all

        #time complexity :O(n)
        #space complexity:O(1)
 
        