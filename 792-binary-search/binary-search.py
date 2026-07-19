class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid #return index value
            if nums[mid]>target: #search in the left half
                high=mid-1
            else:# search in the right half
                low=mid+1  
        return -1   #if element not found return -1           
    #time complexity  O(logn)
    #space complexity  O(1)

        