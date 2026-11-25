class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        #brute force approach
        ans=[]
        window=deque()
        for i ,num in enumerate(nums):
            #checking that element is the part of the current window or not
            while window and window[0]<=i-k:
                window.popleft()
            while  window and nums[window[-1]]<num: #comparing with the last eleemnt of deque
                window.pop()
            window.append(i)
            #after completing first window start appending
            if i>=k-1:
                ans.append(nums[window[0]]) 
        return ans            

      #time complexity:O(n)
      #space complexity:O(n) #using ans list to push

        