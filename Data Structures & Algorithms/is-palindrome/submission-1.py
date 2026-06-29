class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.lower()
        s2=""
        for c in s:
            if c.isalnum():
                s2+=c.lower()      
        for i in range(len(s2)):
            if not s2[i].lower()==s2[len(s2)-1-i].lower():
                return False
        return True