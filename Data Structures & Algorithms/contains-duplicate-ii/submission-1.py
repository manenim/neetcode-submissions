class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # nums = [1,2,3,1]  k = 3
        # {1: 0, 2: 1, 3: 2} we loop through to create a hashmap wher elem is key and index is value
        # but before we add we check
        # have we seen this number before if yes  we subtract the current index from the value if its not <= k we update the val
        # if weve not seen it before, we add it to the hash map and move on
        seen = {}
        for idx, elem in enumerate(nums):
            if elem in seen and idx - seen[elem] <= k:
                return True
            else:
                seen[elem] = idx
        return False
