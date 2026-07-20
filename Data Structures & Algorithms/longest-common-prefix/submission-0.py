class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        
        template = strs[0]

        for i in range(len(template)):

            for word in strs:

                # we check if we are already past the characters in the word
                if i == len(word):
                    return template[:i]
                
                # we check if the current letter in the template matches the current word letter
                if template[i] != word[i]:
                    return template[:i]
        return template
