class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n-2): #-2 because it will check further 
            if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i+2]!=s[i]:
                ans+=1  #if not equal increase 
        return ans         
        