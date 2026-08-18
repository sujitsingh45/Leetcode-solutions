class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #corner case 
        if len(s)!=len(t):
            return False
        frq={}
        #in string count the frequency
        for i in s:
            if i not in frq:
                frq[i]=1
            else:
                frq[i]+=1  
        # decrease the frequency if its present in the another string ,not return false        
        for i in t:
            if i not in frq:
                return False
            else:
                frq[i]-=1  
        #check all frequency are zero or not if not false        
        for i in frq.values():
            if i!=0:
                return False
        return True

        #time complexity: O(n)
        #space complexity:O(n)
        