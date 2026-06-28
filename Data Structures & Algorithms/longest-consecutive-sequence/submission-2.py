class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        number=0
        conteo=1
        maximo=0
        if len(nums)==0:
            return 0
        for i in range(len(nums)-1):
            number=nums[i]
            if number==nums[i+1]:
                continue
            if number+1==nums[i+1] :
                conteo+=1
            else:
                maximo=max(maximo, conteo)
                conteo=1
        maximo=max(maximo, conteo)

        return maximo