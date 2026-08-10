class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()# make it the list 
        right=len(s)-1
        left=0
        # swpap by using two pointer
        while left<right:
            temp=s[left]
            s[left]=s[right]
            s[right]=temp
            left+=1
            right-=1
        return" ".join(s) #return again string with one space
         

        