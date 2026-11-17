class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            area=min(height[left],height[right])*(right-left) #calculating the area
            if area>max_area: #updating the area
                max_area=area
            if height[left]>height[right]: #move the pointer if its less
                right=right-1
            else:
                left=left+1
        return max_area #return max area

        #time complexity:O(n)
        #space complexity:O(1)


            




        