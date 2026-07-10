class Solution(object):
    def isPowerOfThree(self, n):
        #base case 
        if n<=0:
            return False
        if n==1:
            return True    
        if n%3!=0:
            return False
        #recursion case
        return self.isPowerOfThree(n//3)               
        
        