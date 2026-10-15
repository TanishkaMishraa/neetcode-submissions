class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        l = 0 
        max_len = 0
        max_freq = 0

        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            max_freq = max(cnt.values())

            while (r - l + 1) - max_freq > k:
                cnt[s[l]] -= 1
                l += 1
                
            max_len = max(max_len, r - l + 1)
           

        return max_len    