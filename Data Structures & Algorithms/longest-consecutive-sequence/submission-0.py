class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        
        res = 0
        for i in num:
            cnt = 1
            if i - 1 not in num:
                n = i 
                while n + 1 in num:
                    cnt += 1
                    n += 1

            res = max(res, cnt)        

        return res    