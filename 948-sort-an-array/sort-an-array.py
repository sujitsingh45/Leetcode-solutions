
class Solution:
    def merge_two_l(self,a,b):
        sorted_list=[]
        i=0
        j=0
        len_a=len(a)
        len_b=len(b)
        while i<len_a and j<len_b:
            if a[i]>=b[j]:
                sorted_list.append(b[j])
                j+=1
            else:
                sorted_list.append(a[i])
                i+=1
        while i<len_a:
            sorted_list.append(a[i])
            i+=1
        while j<len_b:
            sorted_list.append(b[j])
            j+=1   
        return sorted_list

     

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left=nums[:mid] #taking  first half array 
        right=nums[mid:] #taking last half array
        left=self.sortArray(left) 

        right=self.sortArray(right)
        return self.merge_two_l(left,right)  

        #time complexity: O(nlogn)
        #space complexity:O(n)  
       