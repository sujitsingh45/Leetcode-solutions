class Solution:
    def search(self, matrix: list[list[int]], target: int,midrow) -> bool:#maintain the order of the argument
        c=len(matrix[0]) #size of columns
        start=0 #starting pointer 
        end=c-1 #ending pointer
        while start<=end:
            midc=start+(end-start)//2
            if matrix[midrow][midc]==target:
                return True
            elif target> matrix[midrow][midc]:
                start=midc+1
            else:
                end=midc-1   
        return False         
                 

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False
        #apply bs on rows 
        rows=len(matrix)#no of rows
        cols=len(matrix[0]) #no of columns
        left=0
        right=rows-1
        while left<=right:
            midrow=left+(right-left)//2
            if target>=matrix[midrow][0] and target<=matrix[midrow][cols-1]:
                return self.search(matrix,target,midrow) #search in that

            elif target >matrix[midrow][cols-1]:#search downside
                left=midrow+1 


            else: #search upside
                right=midrow-1
        return False    

        #time complexity:O(olog(nxm))      
        #space complexity:O(1)        
        