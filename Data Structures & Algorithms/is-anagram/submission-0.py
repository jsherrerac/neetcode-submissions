class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        r={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in t:
            if i in r:
                r[i]+=1
            else:
                r[i]=1
        if d==r:
            return True
        return False