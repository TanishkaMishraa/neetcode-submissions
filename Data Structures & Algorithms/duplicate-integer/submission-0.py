class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for j in freq.values():
            if j > 1:
                return True  
        return False       