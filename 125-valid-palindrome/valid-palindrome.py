
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch=[]
        for i in s:
            if i.isalnum(): #checking all alphanumeric number
                ch.append(i.lower())

        for i in range(len(ch)//2): #checking the palindrome
            if ch[i]!=ch[-i-1]:
                return False
        return True # return if true

        '''
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True'''



       