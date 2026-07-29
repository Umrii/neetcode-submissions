class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean=""
        for c in s:
            if c.isalnum():
                clean += c

        left=0
        right=len(clean)-1
        
        while left<right:
            if clean[left]==clean[right]:
                left=left+1
                right=right-1

            else:
                return False
        return True
        


        
    


        
        