class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s)
        left=0# at starting index
        for right in range(len(s)+1):# +1 for after last word
            if right==len(s)or s[right]==" ":
                k=right-1
                #reverse using double pointer
                while left<k:
                    temp=s[left]
                    s[left]=s[k]
                    s[k]=temp
                    left+=1
                    k-=1
                left=right+1 #update the left for next word
        return "".join(s)   
        # time complexity: O(n) 
        # space complexity: 0(n) because of converting string to list    

                 
        