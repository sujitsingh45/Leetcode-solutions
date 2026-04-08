class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n%2!=0:
            return False
        stack=[]     
        for ch in list(s):
            # opening bracket
            if ch=="(" or ch=='{' or ch=="[":
                stack.append(ch)

                # closing bracket
            else:
                if len(stack)==0:
                    return False 
                top=stack.pop()
                # checking this is already closing bracket is present or nt
                if ch==")" and top!='(': 
                      return False
                elif ch=="}" and top!="{":
                       return False
                elif ch=="]" and top!='[':
                       return False
        if len(stack)!=0:
            return False
        else:
            return True                       

        