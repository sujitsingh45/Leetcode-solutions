class Solution(object):
    def isPowerOfFour(self, n):
        """while n%4==0:
            n//=4
        if n==1:
            return True
        else:
            return False        
        """
        #base case 
        if n<=0:
            return False
        if n==1:
            return True
        if n%4!=0:
            return False
        # recusrion case 
        return self.isPowerOfFour(n//4)            
        