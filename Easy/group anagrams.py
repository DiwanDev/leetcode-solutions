class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for a in strs:
            sortedS = ''.join(sorted(a))
            res[sortedS].append(a)
        return list(res.values())