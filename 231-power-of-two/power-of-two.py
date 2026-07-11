class Solution(object):
    def isPowerOfTwo(self, n):
       
        #base case
        if n==1:
            return True
        # handling negative part and 0
        if n <= 0:
            return False
        #the number which is not possible     
        if n%2!=0:
            return False 
        # recursion case 
        return self.isPowerOfTwo(n//2)    

            
        
        