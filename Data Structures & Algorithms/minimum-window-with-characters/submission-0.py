class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = {}
        cnt1 = Counter(t)
        l = 0
        res = (-1, -1)
        res_len = float('inf')
        i, j = 0, len(cnt1)

        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            if s[r] in cnt1 and cnt[s[r]] == cnt1[s[r]]:
                i += 1
            while i == j:
                if (r - l + 1) < res_len:
                    res, res_len = (l, r), (r - l + 1)

                cnt[s[l]] -= 1
                if s[l] in cnt1 and cnt[s[l]] < cnt1[s[l]]:
                    i -= 1
                l += 1

        l, r = res

        return s[l: r+1] if res_len != float("inf") else ''    
                   