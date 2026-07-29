class Solution:
    def isPalindrome(self, s: str) -> bool:
        right=len(s)-1
        left=0
        while left<right:
           
            while left<right and not self.alphanumeric(s[left]):
                left=left+1
            while right>left and not self.alphanumeric(s[right]):
                right=right-1
            if s[left].lower()!=s[right].lower():
                return False
            left=left+1
            right=right-1
        return True

    def alphanumeric(self,s):
        return (ord("A")<=ord(s)<=ord("Z") or
                ord("a")<=ord(s)<=ord("z") or
                ord("0")<=ord(s)<=ord("9"))


        
        