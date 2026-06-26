class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+= f"{len(i)}#{i}"
        return s
    def decode(self, s: str) -> List[str]:
        lista=[]
        longitud=0
        cursor=0
        while cursor<len(s):
            inicio_numero=cursor
            while s[cursor]!="#":
                cursor+=1
            longitud=int(s[inicio_numero:cursor])
            lista.append(s[cursor+1:cursor+longitud+1])
            cursor=longitud+cursor+1
        return lista