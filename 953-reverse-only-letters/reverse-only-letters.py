class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s) #convert to list
        right=len(s)-1
        left=0
        while left<right:
            while left<right and  not s[left].isalpha(): #checking from left side 
                left+=1
            while left<right and not s[right].isalpha():#checking from right side 
                right-=1
            # swapping the alpha numeric element    
            temp=s[left]
            s[left]=s[right]
            s[right]=temp
            left+=1
            right-=1
        return "".join(s)   

        # time complexity: O(n)
        # space complexity:O(n) becuase of conversion to list         
        