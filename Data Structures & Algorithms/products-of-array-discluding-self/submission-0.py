class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        der=[1]*len(nums)
        izq=[1]
        producto=[1]*len(nums)
        for i in range(1,len(nums)):
            izq.append(izq[i-1]*nums[i-1])
        for i in range(len(nums)-2, -1, -1):
            der[i] = der[i+1]*nums[i+1]
        for i in range(len(nums)):
            producto[i]=der[i]*izq[i]
        return producto