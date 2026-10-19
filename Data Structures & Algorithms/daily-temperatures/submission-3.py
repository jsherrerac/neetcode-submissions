class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pila=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while len(pila)!=0 and temperatures[i]>temperatures[pila[-1]]:
                idx=pila.pop()
                res[idx]=i-idx
            pila.append(i)
        return res