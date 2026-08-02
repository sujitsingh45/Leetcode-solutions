class Solution:
    def defangIPaddr(self, address: str) -> str:
        #return address.replace(".","[.]")
        ans=""#taking a null string to replace 
        n=len(address)
        for i in range(n):
            if address[i]!=".":
                ans+=address[i]
            else:
                ans+="[.]"    
        return ans        
            