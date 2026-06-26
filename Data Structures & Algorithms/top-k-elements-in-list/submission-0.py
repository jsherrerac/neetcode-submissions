class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=list(d.items())
        l.sort(key=lambda x: x[1], reverse=True)
        x=l[:k]
        h=[]
        for i in x:
            h.append(i[0])
        return h