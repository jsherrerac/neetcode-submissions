class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pares = sorted(zip(position, speed), reverse=True)
        stack=[]
        
        for par in pares:
            t=(target-par[0])/par[1]
            if len(stack)==0 or t>stack[-1]:
                stack.append(t)
        return len(stack)
            