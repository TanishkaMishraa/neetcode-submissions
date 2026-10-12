class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = {}

        for i , j in enumerate(numbers):
            rem = target - j
            if rem in hash:
                return [hash[rem]+1, i+1]
            hash[j] = i    