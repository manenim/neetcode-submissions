class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dictmap = defaultdict(list)

        for w in strs:
            # sort word
            sorted_word = "".join(sorted(w))

            dictmap[sorted_word].append(w)

        return list(dictmap.values())
            
        