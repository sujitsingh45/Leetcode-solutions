class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        vowels="aeiouAEIOU"
        while left<right:
            while left<right and s[left] not in vowels:  #checking from left side 
            
                left+=1
            while left<right and s[right] not in vowels:#checking from right side
                right-=1   
            temp=s[left]  #swaping
            s[left]=s[right] 
            s[right]=temp
            left+=1
            right-=1
        return "".join(s)        


        