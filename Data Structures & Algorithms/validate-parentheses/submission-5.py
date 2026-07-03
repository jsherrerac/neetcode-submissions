class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        pares = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in ("(", "{", "["):
                l.append(i)
            else:
                if len(l)==0 or l[-1]!=pares[i]:
                    return False
                else:
                    l.pop()
        if len(l)==0:
            return True
        return False