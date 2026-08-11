class Solution:
    def addDigits(self, num: int) -> int:
        #using mathematical solution
        if num<10:
            return num
        return (num-1)%9 +1

        #time complexity:O(1)
        #space complexity:O(1)



        
        '''if num<10:
            return num
        d_sum=0 #to return the sum of the digit    
        while num>0:
            d_sum+=num%10
            num//=10 # floor divison to get  next unit digit
            
        return self.addDigits(d_sum) '''

        