class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_map = defaultdict(int)

        for num in nums:
            nums_map[num] += 1
        
        for key, val in nums_map.items():
            if val > (len(nums) / 2):
                return key
            
        