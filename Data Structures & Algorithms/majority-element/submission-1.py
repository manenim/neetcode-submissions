class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None 

        for n in nums:
            if count == 0:
                candidate = n

            if candidate == n:
                count += 1 # reinforcement 
            else: 
                count -= 1  # killed each other
            
        return candidate  # remaining standing soldier
            
        