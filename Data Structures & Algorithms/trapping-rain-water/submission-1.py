class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        leftM=height[0]
        rightM=height[-1]
        water=0
        while i<j:
            if height[i]<height[j]:    
                if height[i]>=leftM:
                    leftM=height[i]
                else:
                    water+= leftM-height[i]
                i+=1
            else:
                if height[j]>=rightM:
                    rightM=height[j]
                else:
                    water+=rightM-height[j]
                j-=1
        return water