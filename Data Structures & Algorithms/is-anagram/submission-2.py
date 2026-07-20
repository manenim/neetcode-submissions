class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # create a hashmap where chars in s is the key and frequency is the value
        # make a second pass and subtract the value if a char repeats in t 
        # if all is 0 then its an anagram, else its not 
        seen: dict[str, int] = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        print(seen)
        for char in t:
            if char not in seen:
                return False
            seen[char] -= 1
            if seen[char] < 0:
                return False
        return True