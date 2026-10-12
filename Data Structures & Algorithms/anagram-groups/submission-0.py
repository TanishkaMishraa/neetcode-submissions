class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for i in strs:
            key = ''.join(sorted(i))
            hash[key].append(i)

        return list(hash.values())    