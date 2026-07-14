class Solution(object):
    def totalNumbers(self, digits):
        #create one set to avoid to store  duplicate
        s=set()
        n=len(digits)
        #loops
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    #indices must be zero
                    if i==j or j==k or i==k:
                        continue        
                   # No leading zero
                    if digits[i]==0:
                        continue
                    # unit digit must be even    
                    if digits[k]%2!=0:
                        continue

                    num=digits[i]*100+digits[j]*10+digits[k]  
                    s.add(num)
        return len(s)                     