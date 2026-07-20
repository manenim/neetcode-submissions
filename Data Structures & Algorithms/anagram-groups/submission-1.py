class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input: strs = ["act","pots","tops","cat","stop","hat"]

        ans = defaultdict(list)

        for word in strs:
            word_map = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                word_map[index] += 1
            ans[tuple(word_map)].append(word)
        return list(ans.values())

        # ans = default dict{}

        # loop throught strs using  word
        #   word map = [0] * 26
        # we need to convert each word to a number mapping so...
            
            #   we loop through each char in each word using char
                    # index = ord(char) - ord("a")  gives us the index of the letter in word map
                    # wordmap[index] += 1   update the word map
            #  ans[tuple(wordmap)].append(word)

        