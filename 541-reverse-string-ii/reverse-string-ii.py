class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #convert string into list
        char=list(s)
        for i in range(0,len(char),2*k): #iteration on 2*k
            char[i:i+k]=char[i:i+k][::-1] #reverse on k

        return ''.join(char)    #converting into string
        
        #time complexity O(n)
        #space complexity O(n) # bcz we are converting into list and slicing builds a new string



        
        