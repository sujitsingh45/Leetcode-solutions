class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums+=nums # adding list in list to make it circular
        stack=[]
        n=len(nums)  
        result=[-1]*n # initialize result with -1
        # traverse from right to left
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            if stack: # if stack is not empty ,last element is greater element
                result[i]=nums[stack[-1]]
            stack.append(i)
        return result[:len(nums)//2] # now return half list

        # time complexity : o(n)
        # space complexity  :o(1)
        
        