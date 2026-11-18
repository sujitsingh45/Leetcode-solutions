class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        
        
        actual_sum=0
        dict1={}
        for x in grid:
            for y in x:
                actual_sum=actual_sum+y
                if y in dict1:
                    dict1[y]+=1
                else:
                    dict1[y]=1
        
        
        for key,value in dict1.items():
            if value==2:
                repeat=key
                break
        missing=n**2*(n**2 +1)//2+repeat-actual_sum
        return[repeat,missing]        
                




        