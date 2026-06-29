class Solution:
    def isPalindrome(self, s: str) -> bool:
        """s.lower()
        s2=""
        for c in s:
            if c.isalnum():
                s2+=c.lower()      
        for i in range(len(s2)):
            if not s2[i].lower()==s2[len(s2)-1-i].lower():
                return False
        return True"""
        #solución 2
        s= s.lower()
        i=0
        j=len(s)-1
        while i<j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i].isalnum() and s[j].isalnum():
                if not s[i]==s[j]:
                    return False
            i+=1
            j-=1
        return True


