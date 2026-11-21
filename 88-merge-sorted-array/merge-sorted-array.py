class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        #pushing the other list elemnet into the bigger list
        idx=m+n-1
        j=n-1 #last valid element in nums2
        i=m-1 #last valid element in  nums1

        while i>=0 and j >=0:
            if nums1[i]>=nums2[j]: #push into last if the element is greater 
                nums1[idx]=nums1[i] 
                idx=idx-1
                i=i-1
            else:
                nums1[idx]=nums2[j] #push if nums2 elemnt is greater
                j=j-1
                idx=idx-1
             #when i <0 push all element to the nums1
        while j>=0:
                    nums1[idx]=nums2[j]
                    j=j-1
                    idx=idx-1                
                #space complexity:O(n+m)   
                #space complexity:O(1)  requirement of the problem