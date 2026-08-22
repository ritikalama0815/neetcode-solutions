class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for str in strs:
            sortedW = ''.join(sorted(str))
            anagram[sortedW].append(str)

        return list(anagram.values())