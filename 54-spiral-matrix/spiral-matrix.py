class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows=len(matrix)
        cols=len(matrix[0])
        strows=0 
        endrows=rows-1  #ending point of the row
        stcols=0
        endcols=cols-1 #starting and ending point 0f the col
        ans=[]

        while strows<=endrows and stcols<=endcols:
            #left to right #strow is constant here
            for i in range(stcols,endcols+1):
                ans.append(matrix[strows][i])
               
            #top to down where end cols is constant and endrows vary
            for j in range(strows+1,endrows+1):
                ans.append(matrix[j][endcols])
                
            #right to left here enrows is constant
            for i in range(endcols-1,stcols-1,-1):
                if strows==endrows:
                    break
                ans.append(matrix[endrows][i])
                
            #buttom to top here stcols is contstant
            for j in range(endrows-1,strows,-1):
                if stcols==endcols: #to not get duplicate in case of odd matrix
                    break
                ans.append(matrix[j][stcols])
                
            # after calculating all the upper boundary we go to decrease endrows and endcols and increase to strows and stcols, becuse we dont want duplicate and making it spiral
            strows+=1
            endrows-=1
            stcols+=1
            endcols-=1
        return ans    



        