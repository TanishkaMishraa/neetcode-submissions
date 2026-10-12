class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_freq = max(freq.values())       

        bucket = [[] for _ in range(max_freq + 1)]

        for i, j in freq.items():
            bucket[j].append(i)

        res= []
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res    