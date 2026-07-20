class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr1 = list(word1)
        arr2 = list(word2)

        merged_arr = []


        p = 0

        while p < max(len(arr1), len(arr2)):
            if p < len(arr1):
                merged_arr.append(arr1[p])
            if p < len(arr2):
                merged_arr.append(arr2[p])
            p += 1
        
        return "".join(merged_arr)