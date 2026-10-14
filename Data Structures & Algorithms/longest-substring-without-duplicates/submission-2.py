class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i = 0
        temp = set()
        for j in range(i , len(s)):
            while s[j] in temp :
                temp.remove(s[i])
                i += 1
            max_len = max(max_len, j - i + 1)    
            temp.add(s[j])

        return max_len        