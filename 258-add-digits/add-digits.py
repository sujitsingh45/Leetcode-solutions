class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        d_sum=0 #to return the sum of the digit    
        while num>0:
            d_sum+=num%10
            num//=10 # floor divison to get  next unit digit
            
        return self.addDigits(d_sum)    


        