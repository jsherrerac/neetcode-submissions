class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retorno=[]
        if len(strs)==1:
            retorno.append(strs)
            return retorno
        elif len(strs)>1:
            d={}
            
            for i in range(len(strs)):
                base="".join(sorted(strs[i]))
                if base not in d:
                    d[base]=[i]
                else:
                    d[base]+=[i]
            for j in d.values():
                temp=[]
                for i in j:
                    temp.append(strs[i])
                retorno.append(temp)                    
            return retorno