class Solution(object):
    def myPow(self, x, n):
        #base case
        if n<0:
            return 1 / self.myPow(x,-n)
        if n==0:
            return 1
        # RECURSIVE CASE 
        a = self.myPow(x,n//2)
        if n%2==0: #if it's even a*a
            return a*a
        else: #if it's odd
            return a*a*x         

        
        