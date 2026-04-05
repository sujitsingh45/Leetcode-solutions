class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacka=[]
        stackb=[]
        for i in list(s):
            if i=="#" :
                if stacka:
                    stacka.pop()  
            else:
                stacka.append(i)
        for i in list(t):
            if i=="#" :
                if stackb:
                    stackb.pop()  
            else:
                stackb.append(i)           
        return  stacka==stackb
        

            # time complexity :o(n+m) for o(n) first loop and for o(m) second loop
             