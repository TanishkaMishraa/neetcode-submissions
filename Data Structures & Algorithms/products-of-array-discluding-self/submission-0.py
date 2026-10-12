class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suf = [1] * len(nums)
        pre = [1] * len(nums)
    
        for i in range(1, len(pre)):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(suf)-2, -1, -1) :
            suf[i] = suf[i+1] * nums[i+1]

        for i in range(len(nums)):
            nums[i] = suf[i] * pre[i]  

        return nums    