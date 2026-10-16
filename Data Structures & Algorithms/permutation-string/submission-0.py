class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = Counter(s1)
        cnt = {}
        max_len = 0
        l = 0 
        for r in range(len(s2)):
            cnt[s2[r]] = cnt.get(s2[r], 0) + 1
            while (r - l + 1) > len(s1):
                cnt[s2[l]] -= 1
                if cnt[s2[l]] == 0:
                    del cnt[s2[l]]
                l += 1
            if cnt1 == cnt:
                return True    

        return False    